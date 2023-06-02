from django.db import models

class Hardware(models.Model):
    category = models.CharField(max_length=100)

class Software(models.Model):
    type= models.CharField(max_length=100)

class Boot(models.Model):
    status = models.CharField(max_length=100)

class Problem(models.Model):
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=100)