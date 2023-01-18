from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

directions = {1: 'one',
              2: 'two',
              3: 'three',
              4: 'four'}


def index(request):
    keys = ''
    for key in directions:
        path = reverse('main-link', args=((key),))
        keys += f"<li> <a href='{path}'> {key} </a> </li>"
    response = '<ul>' + keys + '</ul>'
    return HttpResponse(response)


def numeric_func(request, variable: int):
    value = directions.get(variable, 'soething')
    path = reverse('main-link', args=((value),))
    return HttpResponseRedirect(path)


def func(request, variable: str):
    if variable == 'one':
        return HttpResponse('respose_one')
    if variable == 'two':
        return HttpResponse('respose_two')
    return HttpResponseNotFound(f'{variable}')
