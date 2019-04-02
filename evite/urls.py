from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.test import SimpleTestCase, override_settings
from django.conf.urls.static import static

from . import views
from .views import ListEventView


app_name = 'evite'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('createEvent/', views.createEvent, name='createEvent'),
    path('fillProfile/', views.fillProfile, name='fillProfile'),
    path('viewEvent/', views.viewEvent, name='viewEvent'),
	path('viewEvent/<int:eventid>', views.viewEventDesc, name='viewEventDesc'),
	path('participantForm/<int:eventid>', views.participantForm, name='participantForm'),
    path('event/', ListEventView.as_view(), name="event-all"),
    path('rsvp/<int:eventid>', views.rsvp, name='rsvp'),
    path('rsvp-reply/<int:token>', views.replyRSVP, name='rsvp-reply'),
]
