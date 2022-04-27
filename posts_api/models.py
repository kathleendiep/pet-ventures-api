from django.db import models
from datetime import date
# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=32)
    category = models.CharField(max_length=32)
    breed = models.CharField(max_length=32)
    info = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    img = models.CharField(max_length=100, blank=True, null=True, default="")
    # image = models.CharField(max_length=100, blank=True, null=True, default="")
    # pub_date = models.DateField(null=True, blank=True)
    # user = models.ForeignKey(User, related_name='posts')

