from django.db import models


class anim(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.IntegerField()
    ownername = models.CharField(max_length=100)
 
def __str__(self):
    return self.name


# Create your models here.
