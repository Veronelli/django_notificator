from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def notification_page(request: HttpRequest)->HttpResponse:
    return render(request, 'notification_page.html')