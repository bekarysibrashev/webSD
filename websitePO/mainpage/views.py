from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'mainpage/index.html')
# Create your views here.

def about_group(request):
    return render(request, 'mainpage/about_group.html')