from django.shortcuts import render
from django.db.models import Count
from .models import *

def index(request, params=None):
    return render(request, 'menu/index.html')
