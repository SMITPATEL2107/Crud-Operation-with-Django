from django.db import models

# Create your models here.
class user(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    pics = models.ImageField(upload_to="img/",default="abc.jpg")