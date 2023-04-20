from django.urls import path, re_path
from .views import *
from django.contrib import admin

app_name = 'app'

urlpatterns = [
    path('', index, name='index'),
    re_path(r'^(.*)/$', index, name='index'),
]
