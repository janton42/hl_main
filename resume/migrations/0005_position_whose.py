# Generated by Django 4.1.7 on 2023-03-10 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cold_apply', '0007_remove_keywordanalysis_created_at_and_more'),
        ('resume', '0004_remove_organization_chronological_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='whose',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cold_apply.participant'),
        ),
    ]
