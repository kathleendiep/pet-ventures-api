# Generated by Django 4.0.4 on 2022-04-26 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts_api', '0004_remove_post_image_post_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='img',
        ),
    ]
