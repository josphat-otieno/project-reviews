from django.db import models
from django.db.models.base import Model

# Create your models here.

class UserProfile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profile/')
    bio = models.TextField()
    phone_number = models.IntegerField()

    