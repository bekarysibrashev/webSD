from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_group', views.about_group, name='about_group'),
    path('about_group/test', views.test, name='test' ),
    path('about_group/developers', views.dev, name='dev')
]


