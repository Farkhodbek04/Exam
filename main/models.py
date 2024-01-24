from django.db import models

class Services(models.Model):
    image = models.ImageField(upload_to='services')
    title = models.CharField(max_length=40, default='Default title')
    body = models.CharField(max_length=255, default='Some default text')    

class Client(models.Model):
    image = models.ImageField(upload_to="clients image")
    name = models.CharField(max_length=35, default='Some default client name')
    opinion = models.CharField(max_length=255,default='Some default opinion')

class Contact(models.Model):
    full_name = models.CharField(max_length=50, default="Some full name")
    email = models.EmailField(max_length=50, default='email')
    phone = models.CharField(max_length=20, default='phone')
    message = models.CharField(max_length=255, default='Message')

class Guard(models.Model):
    image = models.ImageField(upload_to='Guards image')
    name = models.CharField(max_length=30, default="Guard name")
    status = models.CharField(max_length=20, default="Guard status")