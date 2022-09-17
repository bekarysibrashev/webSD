from unicodedata import name
from django.db import models

# Create your models here.

class Participance(models.Model):
    name = models.CharField("Имя", max_length=50)
    age = models.IntegerField("Возраст")
    bio = models.TextField("Биография")

    def __str__(self):
        return self.name

class News(models.Model):
    topic = models.CharField("Зголовок", max_length=50)
    news = models.TextField("Новость")

    def __str__(self):
        return self.topic