from django.db import models

# Create your models here.
class users(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    username=models.EmailField()
    password=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    mobile=models.BigIntegerField()