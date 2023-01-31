from django.db import models
from django.urls import reverse

# Create your models here.

class Table(models.Model):
    char_column = models.CharField(max_length=40)
    int_column = models.IntegerField()

    def __str__(self):
        return f'{self.char_column} - {self.int_column}'

    def get_url(self):
        return reverse('get_link', args=[self.id])
