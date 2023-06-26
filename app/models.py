from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models





class Author(AbstractUser):

    address = models.CharField(max_length=250)
    dob = models.DateField()
    mobile = models.CharField(max_length=30) 
 

   

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)