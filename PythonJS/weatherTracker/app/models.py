from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.core.validators import EmailValidator

# Create your models here.

class Profile(models.Model):
    user = models.CharField(max_length=250, default="", editable=True, unique=True)
    email = models.EmailField(validators=[EmailValidator()],  default="")
    def __str__(self):
        return self.user
class Search(models.Model):
    searchTerm = models.CharField(max_length=250, default="")
    def __str__(self):
        return self.searchTerm
# class Profile(models.Model):
#     user = models.TextField(max_length=250, default="", editable=True, unique=True)
#     email = models.EmailField(validators=[EmailValidator()])
#     def __str__(self):
#         return self.user
# class Search(models.Model):
#     searchTerm = models.CharField(max_length=250, default="")
#     def __str__(self):
#         return self.searchTerm