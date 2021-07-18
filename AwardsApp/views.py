from django.shortcuts import render, redirect, get_object_or_404,get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile, Project, Rating
from django.http import Http404
from .forms import EditProfileForm, ProfileUpdateForm, ProjectForm

# Create your views here.
# @login_required(login_url='/accounts/login/')
def index(request):
    all_projects = Project.objects.reverse()
    return render(request, 'awards/index.html', {"all_projects":all_projects})

def project_detail(request, project_id):
    try:
        project = Project.objects.get(id = project_id)
        
        
    except Project.DoesNotExist:
        raise Http404()

    return render(request,"awards/project_detail.html", {"project":project})

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


def profile_view(request):
    user = request.user
    user = User.objects.get(username = user.username)

    return render (request, 'awards/profile.html', {"user":user})

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

# def search(request):
#     if request.method == 'GET':
#         project_title = request.GET.get("project_title")
#         results = Project.objects.filter(project_title__icontains=project_title).all()
#         message = f'name'
#         context= {
#             'results': results,
#             'message': message
#         }
#         return render(request, 'awards/search.html', context)
#     else:
#         message = "You haven't searched for any Project"
#     return render(request, 'awards/search.html', {'message': message})


def search(request):
    
    if 'projects' in request.GET and request.GET["projects"]:
        search_term = request.GET.get("projects")
        searched_projects = Project.search_project(search_term)
        message = f"{search_term}"

        return render(request, 'awards/search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any project"
        return render(request, 'awards/search.html',{"message":message})

