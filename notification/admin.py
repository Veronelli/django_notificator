from django import forms
from django.contrib import admin

from notification.models import Notification


# Register your models here.
class SendNotificationForm(forms.Form):
    message = forms.CharField(label="Notification Message", max_length=200)
    
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    add_form_template = 'admin/custom_add_form.html'
