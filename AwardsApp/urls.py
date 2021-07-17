from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^api/movie/$', views.MovieList.as_view()),
    # url(r'^api/book/$', views.BookList.as_view())
]
