# Generated by Django 4.0.4 on 2022-04-29 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_profile_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='info',
        ),
    ]
