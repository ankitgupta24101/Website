from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Home


def members(request):
    return HttpResponse("Hello world!")


def home(request):
    mymembers = Home.objects.all().values()
    template = loader.get_template('home.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
  mymember = Home.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))