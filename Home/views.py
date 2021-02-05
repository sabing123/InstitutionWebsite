from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from twilio.rest import Client
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages

from .models import Aboutus, Blog


# Create your views here.

def index(request):
    return render(request, 'index.html')


def blog(request):
    blog1 = Blog.objects.all()
    return render(request, "blog.html", {'blog1': blog1})


def contact(request):
    name=''
    email=''
    phone=''
    subject=''
    message=''
    form= ContactForm(request.POST or None)
    if form.is_valid():
        name= form.cleaned_data.get("name")
        email= form.cleaned_data.get("email")
        phone= form.cleaned_data.get("phone")
        subject= form.cleaned_data.get("subject")
        message=form.cleaned_data.get("message")
        message= name + " with the email, " + email + ", sent the following message:\n\n" + message;
        mail='rupesh.thapa2050@gmail.com'
        send_mail(subject, message,'',[mail])
        context= {'form': form}
        messages.info(request, 'Your message has been sent.')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        context= {'form': form}
    return render(request, 'contact.html', context)


def aboutus(request):
    ab1 = Aboutus.objects.filter(about_category='MaxPro Computer')
    ab2 = Aboutus.objects.filter(about_category='About Us')
    ab3 = Aboutus.objects.filter(about_category='About Classes')
    params = {'ab1': ab1, 'ab2':ab2,'ab3':ab3}
    return render(request, 'about.html', params)
