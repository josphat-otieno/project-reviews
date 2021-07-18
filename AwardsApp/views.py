from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
# @login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'awards/index.html')

def profile_view(request):
    user = request.user
    user = User.objects.get(username = user.username)

    return render (request, 'awards/profile.html', {"user":user})
