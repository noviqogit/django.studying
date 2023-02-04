from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Table3(models.Model):
    char_column = models.CharField(max_length=40)
    char_column2 = models.CharField(max_length=100)


class Table2(models.Model):
    another_column = models.CharField(max_length=40, null=True)


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
    int_column2 = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(100)])
    slug = models.SlugField(default='', null=False, db_index=True)
    choice = models.CharField(max_length=2, choices=BUTTOM_CHOICES, default=FRESHMAN)
    foreign_column = models.ForeignKey(Table2, on_delete=models.PROTECT, null=True)
    foreign_column2 = models.ManyToManyField(Table3)

    def __str__(self):
        return f'{self.char_column} - {self.int_column}'

    def get_url(self):
        return reverse('get_link', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.char_column)
        super().save(args, kwargs)
