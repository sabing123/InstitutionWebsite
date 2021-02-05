from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from twilio.rest import Client

from .models import Aboutus, Blog


# Create your views here.

def index(request):
    return render(request, 'index.html')


def blog(request):
    blog1 = Blog.objects.all()
    return render(request, "blog.html", {'blog1': blog1})


def contact(request):
    return render(request, 'contact.html')


def aboutus(request):
    ab1 = Aboutus.objects.filter(about_category='MaxPro Computer')
    ab2 = Aboutus.objects.filter(about_category='About Us')
    ab3 = Aboutus.objects.filter(about_category='About Classes')
    params = {'ab1': ab1, 'ab2':ab2,'ab3':ab3}
    return render(request, 'about.html', params)
