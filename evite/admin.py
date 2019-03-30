from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from .models import event, participant, organiser,Ticket,rsvp
from .forms import EventInviteListForm,ParticipantForms

# Register your models here.
"""
class EventInviteList(ChangeList):
    def __init__(self, request, model, list_display,list_display_links, list_filter, date_hierarchy,search_fields, list_select_related, list_per_page,list_max_show_all, list_editable, model_admin):

        super(OrganiserInviteList, self).__init__(request, model,list_display, list_display_links, list_filter,date_hierarchy, search_fields, list_select_related,list_per_page, list_max_show_all, list_editable,model_admin)

        # these need to be defined here, and not in MovieAdmin
        self.list_display = ['action_checkbox', 'name', 'attendee']
        self.list_display_links = ['name']
        self.list_editable = ['attendee']

class EventAdmin(admin.ModelAdmin):

    def get_changelist(self, request, **kwargs):
        return EventInviteList

    def get_changelist_form(self, request, **kwargs):
        return EventInviteListForm
"""

class EventAdmin(admin.ModelAdmin):
    model= event
    filter_horizontal = ('attendee',)


#admin.site.register(event)
admin.site.register(participant)
admin.site.register(event, EventAdmin)
admin.site.register(organiser)
admin.site.register(Ticket)
admin.site.register(rsvp)
