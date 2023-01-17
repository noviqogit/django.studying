from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.


def func(request, variable):
    if variable == 'one':
        return HttpResponse('respose_one')
    if variable == 'two':
        return HttpResponse('respose_two')
    return HttpResponseNotFound(f'{variable}')
