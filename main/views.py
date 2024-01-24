from django.shortcuts import render, redirect
# from .models import Services, Contact, Client, Guard
from . import models

# HTML files

def index(request):
    services = models.Services.objects.all()
    clients = models.Client.objects.all()
    guards = models.Guard.objects.all()
    clients = models.Client.objects.all()
    
    context = {
        'services': services,
        'clients': clients,
        'guards': guards,
        'clients': clients
    }

    return render(request, 'front/index.html', context)

def about(request):

    return render(request, 'front/about.html')

def contact(request):    

    return render(request, 'front/contact.html')

def guard(request):
    guards = models.Guard.objects.all()
    return render(request, 'front/guard.html', {'guards': guards})

def service(request):
    services = models.Services.objects.all()
    
    return render(request, 'front/service.html', {'services': services})

def user_message(request):
    if request.method == 'POST':
        models.Contact.objects.create(
            full_name = request.POST['fish'],
            email = request.POST['email'],
            phone = request.POST['number'],
            message = request.POST['message']
        )
        return redirect('index')




