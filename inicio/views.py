from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

def inicio(request):
    return render(request, 'inicio/index.html')