from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.test import SimpleTestCase, override_settings
from django.conf.urls.static import static

from . import views


app_name = 'evite'

urlpatterns = [
    path('', views.index, name='index'),
]
