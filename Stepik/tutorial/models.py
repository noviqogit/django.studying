from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class Table(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    BUTTOM_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]
    char_column = models.CharField(max_length=40)
    int_column = models.IntegerField(null=True, blank=True)  # позволяет сохранять пустые значения
    int_column2 = models.IntegerField(default=0)
    slug = models.SlugField(default='', null=False, db_index=True)
    choice = models.CharField(max_length=2, choices=BUTTOM_CHOICES, default=FRESHMAN)

    def __str__(self):
        return f'{self.char_column} - {self.int_column}'

    def get_url(self):
        return reverse('get_link', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.char_column)
        super().save(args, kwargs)
