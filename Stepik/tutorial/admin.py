from django.contrib import admin, messages
from .models import Table
from django.db.models import QuerySet


# admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['char_column',  # первое значение является ссылочным, нельзя редактировать
                    'int_column',
                    'int_column2',
                    'annotaton',
                    'choice'
                    ]
    list_editable = ['int_column',
                     'int_column2',
                     'choice'
                     ]
    ordering = ['int_column',
                'int_column2',
                ]
    list_per_page = 5
    actions = ['action_one']
    search_fields = ['char_column__startswith', 'choice']
    list_filter = ['char_column',
                   'int_column2',
                   'choice'
                   ]

    @admin.display(ordering='int_column', description='status')
    def annotaton(self, row: Table):
        if not row.int_column2:
            return 'null'
        if row.int_column2 < 20:
            return '< 20'
        return '>= 20'

    @admin.action(description='set_row  ')
    def action_one(self, request, queryset: QuerySet):
        count = queryset.update(choice=Table.JUNIOR)
        self.message_user(request,
                          f'changed {count} objects',
                          messages.ERROR)


# Register your models here.
admin.site.register(Table, TableAdmin)
