from django.shortcuts import render
from .models import Participance, NewText

def index(request):
    news = NewText.objects.all()
    return render(request, 'mainpage/index.html', {'news' : news})   
# Create your views here.

def about_group(request):
    people = Participance.objects.all()
    return render(request, 'mainpage/about_group.html', {'people' : people})
    