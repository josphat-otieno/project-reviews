from django.shortcuts import render, redirect, get_object_or_404,get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile, Project, Rating
from .forms import EditProfileForm, ProfileUpdateForm

# Create your views here.
# @login_required(login_url='/accounts/login/')
def index(request):
    all_projects = Project.objects.reverse()
    return render(request, 'awards/index.html', {"all_projects":all_projects})

def create_project(request):
    pass

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

def search_project(request):
    if request.method == 'GET':
        project_title = request.GET.get("project_title")
        results = Project.objects.filter(title__icontains=project_title).all()
        message = f'name'
        context= {
            'results': results,
            'message': message
        }
        return render(request, 'awards/search.html', context)
    else:
        message = "You haven't searched for any Project"
    return render(request, 'awards/search.html', {'message': message})
