from django.db import models
from datetime import date
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=32)
    category = models.CharField(max_length=32)
    breed = models.CharField(max_length=32)
    info = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    # img = CloudinaryField('image', default="image")
    img = models.CharField(max_length=1000, default="")
    image = models.CharField(max_length=1000, default="")
    # img = models.CharField(max_length=100, blank=True, null=True, default="")
    # pub_date = models.DateField(null=True, blank=True)
    # user = models.ForeignKey(User, related_name='posts')

