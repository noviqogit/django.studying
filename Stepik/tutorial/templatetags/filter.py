from django import template

register = template.Library()


@register.filter(name='filter-name')
def func():
    pass
