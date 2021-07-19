
import json
import re
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Avg
from django.http import Http404, HttpResponse, QueryDict, response
from django.shortcuts import (get_list_or_404, get_object_or_404, redirect,
                              render)
from rest_framework import serializers
from rest_framework.decorators import APIView, api_view
from rest_framework.serializers import Serializer
from .forms import EditProfileForm, ProfileUpdateForm, ProjectForm, RatingsForm
from .models import Project, Rating, UserProfile
from .serializer import ProjectSerializer
from rest_framework.response import Response


# Create your views here.
# @login_required(login_url='/accounts/login/')
def index(request):
    all_projects = Project.objects.reverse().annotate(
        avg_design = Avg('rating__design'),
        avg_usability = Avg('rating__usability'),
        avg_content=Avg('rating__content'),
    )
    return render(request, 'awards/index.html', {"all_projects":all_projects})

def project_detail(request, project_id):
    try:
        project = Project.objects.get(id = project_id)  
    
    except Project.DoesNotExist:
        raise Http404()

    return render(request,"awards/project_detail.html", {"project":project})

# @login_required(login_url='/accounts/login/')
def new_project(request):
    current_user =request.user
    if request.method == 'POST':
        project_form = ProjectForm(request.POST,request.FILES)
        if project_form.is_valid():
            project = project_form.save(commit = False)
            project.userprofile = current_user
            project.save()
            return redirect("index")

    else:
        project_form = ProjectForm()
    return render (request, 'awards/new_project.html', {"project_form":project_form})

# @login_required(login_url='/accounts/login/')
def delete_project(request, project_id):
    item = Project.objects.get(id =project_id)
    if request.method =='POST':
        item.delete()
        return redirect('/')
    return render(request, 'awards/delete.html', {"item":item})
   
# @login_required(login_url='/accounts/login/')
def update_project(request, project_id):
    project = Project.objects.get(id=project_id)
    update_form = ProjectForm(instance=project)
    context = {"update_form": update_form}
    if request.method =="POST":
        update_form = ProjectForm(request.POST, instance = project)
        if update_form.is_valid():
            update_form.save()
            return redirect("/")

    return render (request, 'awards/update_project.html', context)

# @login_required(login_url='/accounts/login/')
def profile_view(request):
    user = request.user
    user = User.objects.get(username = user.username)

    return render (request, 'awards/profile.html', {"user":user})

# @login_required(login_url='/accounts/login/')
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        user_form=EditProfileForm(request.POST, request.FILES,instance =request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # messages.success(request, f'Your profile was updated successfuly')
            return redirect('profile')
    else:
        user_form=EditProfileForm(instance =request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)

        context = {"user_form":user_form, "profile_form":profile_form, "user":user}
        return render(request, 'awards/edit_profile.html', context)

# @login_required(login_url='/accounts/login/')
def search(request):
    
    if 'projects' in request.GET and request.GET["projects"]:
        search_term = request.GET.get("projects")
        searched_projects = Project.search_project(search_term)
        message = f"{search_term}"

        return render(request, 'awards/search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any project"
        return render(request, 'awards/search.html',{"message":message})

def rating(request, project_id):
    user = request.user
    project = Project.objects.get(id=project_id)
    if request.method == 'POST':
        rating_form = RatingsForm(request.POST, request.FILES, instance=project)
        if rating_form.is_valid():
            rating = rating_form.save(commit = False)
            rating.save()
            return redirect('index')
    else:
        rating_form = RatingsForm()

    return render(request, 'awards/rate.html' ,{"user":user, "rating_form":rating_form})

class ProjectList(APIView):
    user = User.objects.all()
    def get(self, request, format=None):
        projects = Project.objects.all()
        serializers = ProjectSerializer(projects, many=True)
        return Response(serializers.data)

# def delete_project(request):
#     if request.method == 'DELETE':
#         project = Project.objects.get(pk=int(QueryDict(request.body).get('project_id')))
#         project.delete()

#         response_data ={}
#         response_data['msg'] = 'Project was deleted successfully'
#         return HttpResponse(
#             json.dumps(response_data),
#             content_type="application/json"
#         )
#     else:
#         return HttpResponse(
#             json.dumps({"nothing to see": "this isn't happening"}),
#             content_type="application/json"
#         )

# @api_view(['GET', 'POST'])
# def project_collection(request):
#     if request.method == 'GET':
#         projects = Project.objects.all()
#         serializer = ProjectSerializer(projects, many=True)
#         return Response(serializer.data)

#     elif request.method== 'POST':
#         pass

