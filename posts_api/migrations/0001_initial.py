# Generated by Django 4.0.4 on 2022-04-25 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('category', models.CharField(max_length=32)),
                ('breed', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=2000)),
            ],
        ),
    ]
