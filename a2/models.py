from django.db import models


# Create your models here.

class Places(models.Model):
   name:str
   cap:str
   review:int
   days:int
