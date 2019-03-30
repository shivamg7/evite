from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.

class participant(models.Model):

    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    phone = models.CharField(primary_key=True, max_length=10)

    def __str__(self):
        return self.name


class organiser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    company = models.CharField(max_length=20)
    image = models.ImageField(upload_to='organisers',blank=True)


    def __str__(self):
        return self.name


class event(models.Model):

    CATEGORY_CHOICES = (
        ('CONF','Conference'),
        ('WORK','Workshops & Training'),
        ('FEST','College Fest'),
        ('SPRT','Sports Event'),
        ('ENTR','Entertainment Events'),
        ('REUN','Reunions'),
        ('TREK','Treks & Trips'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    startDate = models.DateField(default=datetime.today)
    endDate = models.DateField(default=datetime.today)
    city = models.CharField(max_length=20,default='Bangalore')
    Venue = models.TextField()
    category = models.CharField(max_length=4,choices=CATEGORY_CHOICES)
    createdBy = models.ForeignKey(organiser,default=None,on_delete=models.CASCADE)
    ticketPrice = models.IntegerField(default=0)
    image = models.ImageField(upload_to='events',blank=True)
    description = models.TextField()
    attendee = models.ManyToManyField(participant)

    def __str__(self):
        return self.name


class rsvp(models.Model):
    RSVP_CHOICES = (
        ('ATT','Attending'),
        ('NAT','Not Attending'),
        ('NSU','Not Sure'),
        ('NDA','Not Filled')
    )
    eventV = models.ForeignKey(event,on_delete=models.CASCADE)
    token = models.CharField(max_length=10)
    status = models.CharField(max_length=3,choices=RSVP_CHOICES)
