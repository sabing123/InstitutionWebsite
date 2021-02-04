from django.urls import path
from . import views

urlpatterns = [
    path('contactview', views.contactview, name='contactview'),
]