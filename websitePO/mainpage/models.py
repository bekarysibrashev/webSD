from django.db import models

# Create your models here.
class Participance(models.Model):
    name = models.CharField("Имя", max_length=50)
    age = models.IntegerField("Возраст")
    bio = models.TextField("Биография")

    def __str__(self):
        return self.name

class NewText(models.Model):
    topic = models.CharField("Тема", max_length=50)
    info = models.CharField("Заголовок", max_length=1000)

    def __str__(self):
        return self.topic