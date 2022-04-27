# Generated by Django 4.0.4 on 2022-04-27 19:11

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts_api', '0004_post_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='img',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image'),
        ),
    ]
