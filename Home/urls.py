from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.aboutus, name='about'),
    path(r'broadcast', views.broadcast_sms, name="default"),
]