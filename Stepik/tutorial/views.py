from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


# Create your views here.

def numeric_func(request, variable: int):
    directions = {1: 'one', 2: 'two'}
    value = directions.get(variable, 'soething')
    return HttpResponseRedirect(f'/resource/{value}')


def func(request, variable: str):
    if variable == 'one':
        return HttpResponse('respose_one')
    if variable == 'two':
        return HttpResponse('respose_two')
    return HttpResponseNotFound(f'{variable}')
