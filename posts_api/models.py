from django.db import models

# Create your models here.
class Post(models.Model):
    Name = models.CharField(max_length=32)
    Category = models.CharField(max_length=32)
    Breed = models.CharField(max_length=32)
    Description = models.CharField(max_length=200)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    img = models.CharField(max_length=2000)
