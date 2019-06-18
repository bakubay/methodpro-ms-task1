from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    username = models.CharField(max_length=16, unique=True)
    age = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.firstname} / {self.lastname} / {self.age} "