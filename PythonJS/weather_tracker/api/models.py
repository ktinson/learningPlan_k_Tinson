from django.db import models
from django.core.validators import validate_email

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=10, unique=True, default="")
    password = models.CharField(max_length=10, unique=False, default="")
    email = models.EmailField( max_length = 254, validators=[validate_email])
    def __str__(self):
        return self.username
class Search(models.Model):
    searchTerm = models.CharField(max_length=100, default="")
    def __str__(self):
        return self.searchTerm