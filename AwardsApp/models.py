from django.db import models
from django.db.models.aggregates import Max
from django.db.models.base import Model
from django.core.validators import MinValueValidator, MaxValueValidator

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

class Rating(models.Model):
    design = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=0)
    usability = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=0)
    content = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=0)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)