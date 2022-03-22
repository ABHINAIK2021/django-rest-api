from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=1024)
    email = models.CharField(max_length=1024)
    subject = models.CharField(max_length=1024)
    message = models.CharField(max_length=1024)