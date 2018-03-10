from django.urls import path, re_path
from blog import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
]