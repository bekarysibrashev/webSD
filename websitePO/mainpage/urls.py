from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_group', views.about_group, name='about_group')
]
