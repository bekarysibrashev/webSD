from django.db import models

# Create your models here.
class Participance(models.Model):
    name = models.CharField("Имя", max_length=50)
    age = models.IntegerField("Возраст")
    bio = models.TextField("Биография")
<<<<<<< HEAD
=======

    def __str__(self):
        return self.name
>>>>>>> 2a9a21addfcb42eec5f427a0f317a630129a821f
