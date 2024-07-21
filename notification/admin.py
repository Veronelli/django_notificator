from django import forms
from django.contrib import admin
from django.http import HttpRequest, HttpResponseRedirect
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.urls import path

from notification.models import Notification
from notification.tasks import send_notification_task


# Register your models here.
class SendNotificationForm(forms.Form):
    message = forms.CharField(label="Notification Message", max_length=200)
    
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    add_form_template = 'admin/custom_add_form.html'
    
    def delete_view(self, request: HttpRequest, object_id: int, extra_context=None):
        notification = Notification.objects.get(pk=object_id)
        message = f'Removed item {object_id}, message"{notification.message}"'
        if request.method == 'POST':
            send_notification_task.delay(message)
        
        return super().delete_view(request, object_id, extra_context)
    
    def add_view(self, request: HttpRequest, form_url = None, extra_context = None):
        if request.method == 'POST':
            form = SendNotificationForm(request.POST)
            if form.is_valid():
                message = form.cleaned_data["message"]
                notification = Notification.objects.create(message=message)
                
                send_notification_task.delay(message)

                return HttpResponseRedirect('../{}/'.format(notification.pk))
        else:
            form = SendNotificationForm()
        new_context = self.get_changeform_initial_data(request)
        new_context['form'] = form
        return super().add_view(request, form_url, extra_context=new_context)

    def get_urls(self):
        urls = super().get_urls()
        custom_url = [
            path("send-notification/", self.admin_site.admin_view(self.add_view), name="send-notification"),
        ]
        return custom_url + urls