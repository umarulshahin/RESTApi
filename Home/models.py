from django.db import models

# Create your models here.

class Team(models.Model):
    team_name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.team_name
    
class People(models.Model):
    team=models.ForeignKey(Team,null=True,blank=True,on_delete=models.CASCADE,related_name="member",default=None)
    name =models.CharField(max_length=100)
    age =models.IntegerField()
    location =models.CharField(max_length=150)
    
    
class User_details(models.Model):
    
    username=models.CharField(max_length=150,null=False)
    email=models.EmailField(null=False)
    password=models.CharField(max_length=150,null=False)