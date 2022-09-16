from unicodedata import name
from django.db import models

# Create your models here.

class Participance(models.Model):
    name = models.CharField("Имя", max_length=50)
    age = models.IntegerField("Возраст")
    bio = models.TextField("Биография")

 