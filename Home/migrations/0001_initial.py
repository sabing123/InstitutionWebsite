# Generated by Django 3.1.3 on 2021-02-04 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_category', models.CharField(default='', max_length=50)),
                ('about_desc', models.CharField(max_length=500)),
                ('about_image', models.ImageField(default='', upload_to='images')),
            ],
        ),
    ]
