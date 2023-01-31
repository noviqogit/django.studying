from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import F, Sum, Max, Min, Count, Avg

# table = Table.objects.all()

# null не учитывается

# Create your views here.
from .models import Table

directions = {
    'key': 'answer',
    'key2': 'answer2',
    'key3': 'answer3'
}

years = {
    1995: 'one',
    2000: 'two',
    3000: 'four'
}


def menu(request):
    # table = Table.objects.order_by('int_column', 'char_column')
    table = Table.objects.order_by(F('int_column').desc(nulls_last=True))
    agg = table.aggregate(Sum('int_column'), Avg('int_column2'), Count('id'))
    # for row in table:
    #     row.save()
    data = {
        'dtl_directions': directions,
        'dtl_table': table,
        'dtl_agg': agg
    }
    response = render(request, 'tutorial/menu.html', context=data)
    return HttpResponse(response)


def get_row(request, name: int):
    row = get_object_or_404(Table, slug=name)
    response = render(request, 'tutorial/page.html', context={'row_dtl': row})
    return HttpResponse(response)


def numeric_func(request, variable: int):
    value = years.get(variable, 'something')
    path = reverse('main-link', args=((value),))
    return HttpResponseRedirect(path)


def page(request, variable: str):
    key = directions.get(variable)
    data = {
        'dtl_key': key,
        'dtl_variable': variable
    }
    response = render(request, 'tutorial/index.html', context=data)
    return HttpResponse(response)
