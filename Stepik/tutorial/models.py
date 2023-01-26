from django.db import models


# Create your models here.

class Table(models.Model):
    char_column = models.CharField(max_length=40)
    int_column = models.IntegerField()
