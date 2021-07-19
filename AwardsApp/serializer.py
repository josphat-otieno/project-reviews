from django.db.models import fields
from rest_framework import serializers
from .models import Project, UserProfile
from django.contrib.auth.models import User


class ProjectSerializer(serializers.ModelSerializer):
    profile = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='username'
    )

    class Meta:
        model = Project
        fields = ('id', 'project_title', 'project_image', 'project_description', 'project_link')
        