# Generated by Django 4.1.5 on 2024-08-23 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeof', models.TimeField()),
                ('date', models.CharField(help_text='Year of experience', max_length=4)),
                ('job_title', models.CharField(max_length=255)),
                ('organization', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
