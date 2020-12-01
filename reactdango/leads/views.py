
from django.http import HttpResponse
from django.template import loader
from re import template
from reactdango.leads.models import ClassName
from django.shortcuts import render

def index(request):
    template =loader.get_template('index.html')
    context = {
        'classnames': ClassName.objects.all()
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
