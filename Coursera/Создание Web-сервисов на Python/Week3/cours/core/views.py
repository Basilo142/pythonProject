from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    return HttpResponse('ok')


def my_view(request):
    t = loader.get_template('myapp/index.html')
    context = {'foo': 'bar'}
    return HttpResponse(t.render(context, request))
