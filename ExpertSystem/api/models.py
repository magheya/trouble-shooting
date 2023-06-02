from django.db import models

# Create your models here.
class Result(models.Model):
    soft=models.CharField(max_length=100,default="")
    hard=models.CharField(max_length=100,default="")
    boot=models.CharField(max_length=100,default="")
    problem=models.CharField(max_length=100,default="")
    solution=models.CharField(max_length=100,default="")
   
