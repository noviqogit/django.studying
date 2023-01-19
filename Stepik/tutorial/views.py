from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

directions = {1: 'one',
              2: 'two',
              3: 'three',
              4: 'four',
              'key': 'answer'}


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
    data = {
        'dtl_directions': directions,
        'dtl_variable': variable
    }
    response = render(request, 'tutorial/index.html', context=data)
    return HttpResponse(response)
