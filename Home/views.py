from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from twilio.rest import Client


# Create your views here.

def index(request):
    return render(request, 'index.html')


def aboutus(request):
    return render(request, 'about.html')


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
