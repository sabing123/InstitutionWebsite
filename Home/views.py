from django.shortcuts import render
from .models import Blog

# Create your views here.

def index(request):
    return render(request, 'index.html')


def blog(request):
    return render(request, 'blog.html')


def blog(request):
    blog1 = Blog.objects.all()
    return render(request, "blog.html", {'blog1': blog1})