from django.db import models

# Create your models here.

class Employees(models.Model):
    user_name = models.CharField(max_length=70)
    age = models.IntegerField()
    adddress = models.TextField()
    joined_date=models.
    last_changes=models.
    relivel_date=models.
