from django.db import models
from django.db.models.base import Model

# Create your models here.

class UserProfile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profile/')
    bio = models.TextField()
    phone_number = models.IntegerField()

class Project(models.Model):
    project_title = models.CharField(max_length= 30)
    project_image = models.ImageField(upload_to = 'images/')
    project_description = models.TextField()
    project_link = models.URLField()
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)