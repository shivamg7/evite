from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
import smtplib



from .forms import EventForm,OrganiserForm

from .models import organiser,participant,event


# Create your views here.


def index(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        userId = User.objects.get(id=request.user.id)
        return render(request, 'evite/index.html', {'user':request.user})
    else:
        return render(request, 'evite/index.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('evite:index'))

def login_(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('evite:index'))

    try:
        log_in = request.POST['login']
    except MultiValueDictKeyError:
        return HttpResponseRedirect(reverse('evite:index'))

    try:
        username = request.POST['username']
        password = request.POST['password']
    except MultiValueDictKeyError:
        error_message = "Missing Credentials"
        return render(request, 'evite/index.html', {'error_message':error_message})

    user = authenticate(request, username=username,password=password)
    if user is not None:
        login(request, user)
        print("login Successful")
        print (user.username)
        return render(request,'evite/index.html',{'user':user})
    else:
        error_message = "Wrong Credentials"
        print("Login Failed")
        return render(request, 'evite/index.html', {'error_message':error_message})

def register(request):

    errors = []
    #Check if the registeration button has been clicked
    try:
        new_registration = request.POST['register']
    except MultiValueDictKeyError:
        return render(request, 'evite/register.html')

    try:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password_1']
        confirm_password = request.POST['password_2']
    except MultiValueDictKeyError:
        errors.append("Missing elements in form.")

    if len(errors)==0:
        if password!=confirm_password:
            errors.append("Passwords do not match.")
            registered = 'False'
        else:
            registered = register_user(username,email,password)
            #try to register user



    if len(errors)==0 and registered=='success':
            user = authenticate(request, username=username,password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('evite:fillProfile'))
    else:
        errors.append(registered)
        return render(request, 'evite/register.html', {'error_message':errors})

def register_user(usr,mail,passcode):

    print("Trying to register user")
    try:
        test_username = User.objects.get(username=usr)
    except User.DoesNotExist:
        user = User.objects.create_user(usr, mail, passcode)
        user.save()
        return "success"

    return "Username is already registered"

def createEvent(request):
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = EventForm(request.POST,request.FILES)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            eventVar = form.save(commit=False)
            eventVar.organiser = organiser.objects.get(name=request.user.username)

            eventVar.save()
            #form.save()
            # redirect to a new URL:
            return HttpResponse("Event Registered")
            #return HttpResponseRedirect(reverse('evite:showEvent',kwargs={'eventId':eventvar.id}))

    # If this is a GET (or any other method) create the default form.
    else:
        form = EventForm()

    return render(request, 'evite/createEvent.html', {'form':form})


def fillProfile(request):

    #Copy to all views
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('evite:index'))

    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = OrganiserForm(request.POST,request.FILES)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            organiserVar = form.save(commit=False)
            # eventVar.organiser =
            organiserVar.email = request.user.email
            organiserVar.name = request.user.username

            organiserVar.save()
            #form.save()
            # redirect to a new URL:
            return HttpResponse("Organiser profile Registered")
            #return HttpResponseRedirect(reverse('evite:showEvent',kwargs={'eventId':eventvar.id}))

    # If this is a GET (or any other method) create the default form.
    else:
        form = OrganiserForm()

    return render(request, 'evite/fillProfile.html', {'form':form})


def viewEvent(request):
    events =  event.objects.all()
    return render(request, 'evite/viewEvent.html',{'events': events})

def viewEventDesc(request,eventid):
    eventvar = event.objects.get(id=eventid)
    venue = str(event.objects.values_list('Venue',flat=True).get(id=eventid))
    params = venue.replace(" ","+")
    params = params.replace(",","%2C")
    return render(request, 'evite/viewEventDesc.html',{'event': event,'params':params})
    

def sendEmails(recepients,event):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("rvceise16@gmail.com", "1rv16isxxx")
    message_body = "HI "+ venue +" "
    for recepient in recepients:
        server.sendmail("rvceise16@gmail.com", recepient, message_body)

    server.quit()
