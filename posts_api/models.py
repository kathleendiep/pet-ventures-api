from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=32)
    category = models.CharField(max_length=32)
    breed = models.CharField(max_length=32)
    info = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    image = models.CharField(max_length=2000, null=True, blank=True)
