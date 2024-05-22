from django.db import models

# Create your models here.


class People(models.Model):
    
    name =models.CharField(max_length=100)
    age =models.IntegerField()
    location =models.CharField(max_length=150)
    
    