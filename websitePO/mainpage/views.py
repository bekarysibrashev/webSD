from django.shortcuts import render
from .models import Participance

def index(request):
    return render(request, 'mainpage/index.html')
# Create your views here.

def about_group(request):
    people = Participance.objects.all()
    return render(request, 'mainpage/about_group.html', {'name' : 'ИМЯ', 'age' : people})
    