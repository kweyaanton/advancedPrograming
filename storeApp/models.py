from django.db import models

# Create your models here.

class Item(models.Model):
    item = models.CharField(max_length=100)
    price = models.CharField(max_length=500)
