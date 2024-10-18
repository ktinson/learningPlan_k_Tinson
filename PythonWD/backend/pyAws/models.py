from django.db import models

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=100, default="")
    description = models.TextField()
    large = models.BooleanField(default=False)
    def __str__(self):
        return self.name