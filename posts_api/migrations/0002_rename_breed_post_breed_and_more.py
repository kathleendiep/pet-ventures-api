# Generated by Django 4.0.4 on 2022-04-22 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Breed',
            new_name='breed',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='City',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='State',
            new_name='state',
        ),
    ]
