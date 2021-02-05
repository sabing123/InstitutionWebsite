from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'index.html')


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