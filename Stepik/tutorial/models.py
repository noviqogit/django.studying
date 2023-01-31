from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Table(models.Model):
    char_column = models.CharField(max_length=40)
    int_column = models.IntegerField()
    slug = models.SlugField(default='', null=False, db_index=True)

    def __str__(self):
        return f'{self.char_column} - {self.int_column}'

    def get_url(self):
        return reverse('get_link', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.char_column)
        super().save(args, kwargs)
