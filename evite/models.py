from django.db import models

# Create your models here.

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
    city = models.CharField(default='Bangalore')
    Venue = models.TextField()
    category = models.CharField(max_length=4,choices=CATEGORY_CHOICES)
    createdBy = models.ForeignKey(organiser,default=None)
    ticketPrice = models.IntegerField(default=0)
    image = models.ImageField(blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class organiser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    company = models.CharField(max_length=20)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name

class participant(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    phone = models.CharField(primary_key=True, max_length=10)

    def __str__(self):
        return self.name
