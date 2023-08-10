from django.db import models


# Create your models here.

class Places(models.Model):
   name = models.CharField(max_length=200)
   cap = models.TextField()
   review = models.IntegerField()
   days = models.IntegerField()
   offer = models.BooleanField(default=False)
