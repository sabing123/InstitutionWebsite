# Generated by Django 3.1.3 on 2021-02-04 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='about_desc',
            field=models.TextField(max_length=500),
        ),
    ]