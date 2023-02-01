from django.contrib import admin, messages
from .models import Table
from django.db.models import QuerySet


class CustomFilter(admin.SimpleListFilter):
    title = 'int2 filter'
    parameter_name = 'int_column2'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'low'),
            ('from 10 to 20', 'medium'),
            ('>=20', 'high'),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<10':
            return queryset.filter(int_column2__lt=10)
        if self.value() == 'from 10 to 20':
            return queryset.filter(int_column2__lte=20, int_column2__gt=10)
        if self.value() == '>=20':
            return queryset.filter(int_column2__gt=20)
        return queryset


# admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    # fields = ['char_column', 'int_column', 'int_column2', 'annotaton', 'choice']
    exclude = ['choice']
    # readonly_fields = ['slug']
    prepopulated_fields = {'slug': ('char_column',)}
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
                   'choice',
                   CustomFilter
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
