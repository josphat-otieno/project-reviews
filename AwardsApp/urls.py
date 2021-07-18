from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('profile/', views.profile_view, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile')
    # url(r'^api/movie/$', views.MovieList.as_view()),
    # url(r'^api/book/$', views.BookList.as_view())
]
