from django import forms
from .models import event,organiser,participant,rsvp


class EventInviteListForm(forms.ModelForm):
    # here we only need to define the field we want to be editable
    participant = forms.ModelMultipleChoiceField(queryset=participant.objects.all(), required=False)


class EventForm(forms.ModelForm):
    class Meta:
        model = event
        fields = ('name', 'startDate', 'endDate', 'city','Venue','category','ticketPrice','image','description')

class OrganiserForm(forms.ModelForm):
    class Meta:
        model = organiser
        fields = ('company','image')

class ParticipantForms(forms.ModelForm):
    class Meta:
        model = participant
        fields = ('name', 'email', 'phone')

class RsvpForm(forms.ModelForm):
    class Meta:
        model = rsvp
        fields = ('tokenPart',)
