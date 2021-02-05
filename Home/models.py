from django.db import models

# Create your models here.

class Blog(models.Model):
    image = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=120)
    date = models.DateField(auto_now=True)
    postedBy = models.TextField(max_length=30)
    description = models.TextField(max_length=200)
