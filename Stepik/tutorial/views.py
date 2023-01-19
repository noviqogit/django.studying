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


def index(request):
    keys = ''
    for key in directions:
        path = reverse('main-link', args=((key),))
        keys += f"<li> <a href='{path}'> {key} </a> </li>"
    response = '<ul>' + keys + '</ul>'
    return HttpResponse(response)


def numeric_func(request, variable: int):
    value = years.get(variable, 'something')
    path = reverse('main-link', args=((value),))
    return HttpResponseRedirect(path)


def page(request, variable: str):
    data = {
        'dtl_directions': directions,
        'dtl_variable': variable
    }
    response = render(request, 'tutorial/index.html', context=data)
    return HttpResponse(response)
