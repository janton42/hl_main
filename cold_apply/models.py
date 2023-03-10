from django.contrib.auth.models import User
from django.db import models

from resume.models import Organization, Overview, Position, Degree, Concentration, Experience, Bullet, Education, \
    CertProjectActivity, LanguageFATS


# Create your models here.

class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    dnc = models.BooleanField(default=False)
    uploaded_resume = models.FileField(upload_to='./cold_apply/static/uploads/', blank=True, null=True)
    uploaded_resume_title = models.CharField(max_length=100, blank=True, null=True)
    veteran = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    current_step = models.ForeignKey('Step', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='created_by', null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='updated_by', null=True)

    def __str__(self):
        return f'{self.name}: {self.email}'

    class Meta:
        verbose_name_plural = 'Participants'


class Interaction(models.Model):
    INTERACTION_TYPES = [
        ('EMAIL', 'EMAIL'),
        ('PHONE', 'PHONE'),
        ('IN_PERSON', 'IN_PERSON'),
        ('OTHER', 'OTHER'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=20, choices=INTERACTION_TYPES, default='EMAIL')
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.participant}: {self.interaction_type}, {self.updated_at}'

    class Meta:
        verbose_name_plural = 'Interactions'


class Job(models.Model):
    STATUSES = [
        ('Open', 'Open'),
        ('Closed', 'Closed'),
    ]
    REASONS = [
        ('In Progress', 'In Progress'),
        ('Employer Closed', 'Employer Closed'),
        ('Candidate Rejected', 'Candidate Rejected'),
        ('Cycle Complete', 'Cycle Complete'),
    ]
    company = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)
    participant = models.ForeignKey(Participant, on_delete=models.SET_NULL, null=True)
    title = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUSES, default='Open')
    status_reason = models.CharField(max_length=20, choices=REASONS, blank=True, null=True)
    application_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='job_created_by', null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='job_updated_by', null=True)

    def __str__(self):
        return f'{self.company}: {self.title}, {self.status}: {self.participant.name}'

    class Meta:
        verbose_name_plural = 'Jobs'


class Application(models.Model):
    STATUSES = [
        ('Submitted', 'Submitted'),
        ('Interview', 'Interview'),
        ('Offer', 'Offer'),
        ('Rejected', 'Rejected'),
        ('Withdrawn', 'Withdrawn'),
    ]
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUSES, default='Submitted')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='application_created_by', null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='application_updated_by', null=True)

    def __str__(self):
        return f'{self.job.participant}: {self.job}, {self.status}'

    class Meta:
        verbose_name_plural = 'Applications'


# TODO: Add a model for the resume. Tailoring will be done by setting FK to resume.Position

class Phase(models.Model):
    title = models.CharField(max_length=200)
    start = models.CharField(max_length=200)
    end = models.CharField(max_length=200)
    result = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Phases'


class Step(models.Model):
    OWNER_CHOICES = [
        ('Participant', 'Participant'),
        ('Hired Labs', 'Hired Labs'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    owner = models.CharField(max_length=20, choices=OWNER_CHOICES, default='Hired Labs')

    def __str__(self):
        return f'{self.title}: {self.phase.title}'

    class Meta:
        verbose_name_plural = 'Steps'


class KeywordAnalysis(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    unigram = models.CharField(max_length=200)
    bigram = models.CharField(max_length=200)
    trigram = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.job}'

    class Meta:
        verbose_name_plural = 'Keyword Analyses'
