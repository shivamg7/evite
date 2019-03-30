from django import forms
from .models import event,organiser,participant


class EventInviteListForm(forms.ModelForm):
    # here we only need to define the field we want to be editable
    participant = forms.ModelMultipleChoiceField(queryset=participant.objects.all(), required=False)
