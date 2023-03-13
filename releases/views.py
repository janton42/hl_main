from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView

from .models import Release, App, Note, Feedback


# Create your views here.
class AppCreateView(LoginRequiredMixin, CreateView):
    model = App
    template_name = 'releases/create_update.html'
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create App'
        return context

    def form_valid(self, form):
        if form.is_valid():
            app = form.save(commit=False)
            app.save()
            return redirect(reverse('releases:index'))
        else:
            print(form.errors)
        return super().form_valid(form)


class ReleasesListView(LoginRequiredMixin, ListView):
    model = Release
    template_name = 'releases/releases_list.html'
    context_object_name = 'releases'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Releases'
        context['now'] = timezone.now()
        return context


class ReleaseDetailView(LoginRequiredMixin, DetailView):
    model = Release
    template_name = 'releases/release_detail.html'
    context_object_name = 'release'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Release'
        return context


class ReleaseCreateView(LoginRequiredMixin, CreateView):
    model = Release
    template_name = 'releases/create_update.html'
    fields = ['app', 'major', 'minor', 'patch']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Release'
        return context

    def form_valid(self, form):
        if form.is_valid():
            release = form.save(commit=False)
            release.author = self.request.user
            release.save()
            return redirect(reverse('releases:index'))
        else:
            print(form.errors)
        return super().form_valid(form)


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'releases/create_update.html'
    fields = ['release', 'text']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Note'
        return context

    def form_valid(self, form):
        if form.is_valid():
            release = form.save(commit=False)
            release.save()
            return redirect(reverse('releases:index'))
        else:
            print(form.errors)
        return super().form_valid(form)


class FeedbackCreateView(LoginRequiredMixin, CreateView):
    model = Feedback
    template_name = 'releases/create_update.html'
    fields = ['feedback']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Feedback'
        return context

    def form_valid(self, form):
        if form.is_valid():
            release = form.save(commit=False)
            release.save()
            return redirect(reverse('releases:index'))
        else:
            print(form.errors)
        return super().form_valid(form)
