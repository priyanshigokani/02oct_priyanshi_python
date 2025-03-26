from django.db import models

class info(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(max_length=20)
