from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

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
    data = {
        'dtl_directions': directions,
    }
    response = render(request, 'tutorial/menu.html', context=data)
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
