from django.db import models

# Create your models here.
class Participance(models.Model):
    name = models.CharField("Имя", max_length=50)
    age = models.IntegerField("Возраст")
<<<<<<< HEAD
    bio = models.TextField("Биография")
=======
    bio = models.TextField("Биография")

    def __str__(self):
        return self.name
>>>>>>> 5c289930fa289b35b380c67cdcac6f4ad2f76888
