from django.db import models


# Create your models here.

class Blog(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=120)
    date = models.DateField(auto_now=True)
    postedBy = models.TextField(max_length=30)
    description = models.TextField(max_length=200)

class Aboutus(models.Model):
    about_id = models.AutoField
    about_category = models.CharField(max_length=50, default="")
    about_desc = models.TextField()
    about_image = models.ImageField(upload_to="images", default="")

    def __str__(self):
        return self.about_category
