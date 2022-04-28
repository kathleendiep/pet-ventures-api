# Generated by Django 4.0.4 on 2022-04-28 01:04

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts_api', '0005_rename_image_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=cloudinary.models.CloudinaryField(default='image', max_length=255, verbose_name='image'),
        ),
    ]
