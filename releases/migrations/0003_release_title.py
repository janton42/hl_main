# Generated by Django 4.1.7 on 2023-03-13 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('releases', '0002_release_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='title',
            field=models.CharField(default='First', max_length=50),
            preserve_default=False,
        ),
    ]
