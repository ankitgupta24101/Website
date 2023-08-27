from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Home


def members(request):
    return HttpResponse("Hello world!")


def home(request):
    mymembers = Home.objects.all().values()
    template = loader.get_template('myfirst.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))
