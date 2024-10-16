from django.db import models
from django.core.validators import validate_email
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=10, unique=False, default="")
    email = models.EmailField( max_length = 254, validators=[validate_email])
    def __str__(self):
        return self.user.username
class Search(models.Model):
    searchTerm = models.CharField(max_length=100, default="")
    def __str__(self):
        return self.searchTerm