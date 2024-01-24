from django.shortcuts import render, redirect
# from .models import Services, Contact, Client, Guard
from . import models

# HTML files

def index(request):       # This function is for index.html
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
    if request.method == 'POST':
        models.Contact.objects.create(
            full_name = request.POST['fish'],
            email = request.POST['email'],
            phone = request.POST['number'],
            message = request.POST['message'],
            # email_sub = request.POST['email_sub']
        )
        return redirect('index')
    
    if request.method == 'POST':
        models.obunalar.objects.create(

        )
    return render(request, 'front/index.html', context)


def about(request):      # This function is for about.html
    # if request.method == 'POST':
    #     models.obunalar.objects.create(
    #         email_sub = request.POST['email_sub']
    #     )
    #     return redirect('index')
    return render(request, 'front/about.html')


def contact(request):     # This function is for contact.html
    if request.method == 'POST':    
        models.Contact.objects.create(
            full_name = request.POST['fish'],
            email = request.POST['email'],
            phone = request.POST['number'],
            message = request.POST['message'],
            # email_sub = request.POST['email_sub']
        )
        return redirect('index')
    return render(request, 'front/contact.html')


def guard(request):   # This function is for guard.html
    guards = models.Guard.objects.all()
    # if request.method == 'POST':
    #     models.obunalar.objects.create(
    #         email_sub = request.POST['email_sub']
    #     )
    #     return redirect('index')
    return render(request, 'front/guard.html', {'guards': guards})


def service(request):  # This function is for service.html
    services = models.Services.objects.all()
    # if request.method == 'POST':
    #     models.obunalar.objects.create(
    #         email_sub = request.POST['email_sub']
    #     )
    #     return redirect('index')
    return render(request, 'front/service.html', {'services': services})




