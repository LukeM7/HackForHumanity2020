from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=30, default='')
    short_description = models.TextField(max_length=100, default='', blank=True)
    long_description = models.TextField(max_length=500, default='', blank=True)
    start_date = models.DateField('date started')
    image_url = models.URLField(max_length=200, default='', blank=True)

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    name = models.CharField(max_length=30, default='')
    email = models.EmailField(max_length=50, default='')
    phone_number = models.CharField(max_length=20, default='')
    image_url = models.URLField(max_length=200, default='', blank=True)
    github_url = models.URLField(max_length=200, default='', blank=True)
    linkedin_url = models.URLField(max_length=200, default='', blank=True)

    def __str__(self):
        return self.name
