from email import message
from unicodedata import name
from django.db import models
import email

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    message=models.TextField()
