from django.db import models
from django.db.models.aggregates import Max
from django.db.models.base import Model
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to = 'profile/')
    bio = models.TextField()
    phone_number = models.IntegerField()

    def __str__(self):
        return self.user

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


class Project(models.Model):
    project_title = models.CharField(max_length= 30)
    project_image = models.ImageField(upload_to = 'images/')
    project_description = models.TextField()
    project_link = models.URLField()
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def search_project(cls, title):
        return cls.objects.filter(title__icontains=title).all()

class Rating(models.Model):
    design = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=0)
    usability = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=0)
    content = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=0)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.project} Rating' 