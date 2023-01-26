from django.db import models


# Create your models here.

class Table(models.Model):
    char_column = models.CharField(max_length=40)
    int_column = models.IntegerField()

    def __str__(self):
        return f'{self.char_column} - {self.int_column}'
