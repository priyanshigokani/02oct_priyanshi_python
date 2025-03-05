from django.db import models
from django.conf import settings

# Create your models here.
class signup(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    number=models.BigIntegerField()
    pas=models.CharField(max_length=20)
    cpas=models.CharField(max_length=20)

class Author(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    user = models.CharField(max_length=20)  # Link to CustomUser
    email=models.EmailField()
    number=models.BigIntegerField()
    bio=models.TextField()
    is_approved = models.CharField(choices=STATUS_CHOICES, default='Pending',max_length=50)  # Field to track approval status


class Genre(models.Model):
     name = models.CharField(max_length=100, choices=[
        ('Romance', 'Romance'),
        ('Action_Adventure', 'Action & Adventure'),
        ('Mystery_Thriller', 'Mystery & Thriller'),
        ('Biographies_History', 'Biographies & History'),
        ('Children', 'Children'),
        ('Young_Adult', 'Young Adult'),
        ('Fantasy', 'Fantasy'),
        ('Historical_Fiction', 'Historical Fiction'),
        ('Horror', 'Horror'),
        ('Literary_Fiction', 'Literary Fiction'),
        ('Non_fiction', 'Non-fiction'),
        ('Science_Fiction', 'Science Fiction'),
    ])
    
class Book(models.Model):
    auname = models.CharField(max_length=100)  # Link to Author
    booktitle = models.CharField(max_length=255)
    pdate = models.DateField()
    description = models.TextField()
    genre = models.CharField(Genre, max_length=200)
    img = models.ImageField(upload_to='book_images/',default='default.jpg')
    myfile = models.FileField(upload_to='book_pdfs/')
    created_at = models.DateTimeField(auto_now_add=True)




