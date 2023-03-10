# Generated by Django 4.1.7 on 2023-03-09 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cold_apply', '0004_step_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeywordAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unigrams', models.TextField()),
                ('bigrams', models.TextField()),
                ('trigrams', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cold_apply.job')),
            ],
            options={
                'verbose_name_plural': 'Keyword Analyses',
            },
        ),
    ]
