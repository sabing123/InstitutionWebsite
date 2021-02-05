from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from twilio.rest import Client

from .models import Aboutus


# Create your views here.

def index(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')


def aboutus(request):
    ab1 = Aboutus.objects.filter(about_category='MaxPro Computer')
    ab2 = Aboutus.objects.filter(about_category='About Us')
    ab3 = Aboutus.objects.filter(about_category='About Classes')
    print(ab1,ab2,ab3)
    params = {'ab1': ab1, 'ab2':ab2,'ab3':ab3}
    return render(request, 'about.html', params)


def broadcast_sms(request):
    message_to_broadcast = ("Thnk you for selecting our institute. Our Member will shortly Contact you"
                            "yet? Grab it here: https://www.twilio.com/quest")
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
        if recipient:
            client.messages.create(to=recipient,
                                   from_=settings.TWILIO_NUMBER,
                                   body=message_to_broadcast)
    return render(request, 'index.html')
