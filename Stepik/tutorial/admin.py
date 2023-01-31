from django.contrib import admin
from .models import Table


# admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['char_column',  # первое значение является ссылочным, нельзя редактировать
                    'int_column',
                    'int_column2',
                    ]
    list_editable = ['int_column',
                     'int_column2',
                     ]
    ordering = ['int_column',
                'int_column2',
                ]
    list_per_page = 5


# Register your models here.
admin.site.register(Table, TableAdmin)
