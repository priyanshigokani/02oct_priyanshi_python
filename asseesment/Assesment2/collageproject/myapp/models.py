from django.db import models

# Create your models here.
class signup(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    role=models.CharField(max_length=10)


class addTea(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    contact=models.BigIntegerField()

class addStu(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    contact=models.BigIntegerField()

class addSt(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    contact=models.BigIntegerField()

class addB(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    BookName=models.CharField(max_length=100)
    BImg=models.ImageField(upload_to='BookImg/')
    myfile=models.FileField(upload_to="myBook/")
    desc=models.TextField()

class addEve(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    EventTitle=models.CharField(max_length=100)
    date=models.DateField()
    img=models.ImageField(upload_to='eveImg')
    desc=models.TextField()
