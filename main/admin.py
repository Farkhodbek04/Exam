from django.contrib import admin
from .models import Services, Client, Contact, Guard

class ShowServices(admin.ModelAdmin):
    list_display = ('image', 'title', 'body')
admin.site.register(Services, ShowServices)

class ShowClient(admin.ModelAdmin):
    list_display = ('image', 'name', 'opinion')
admin.site.register(Client, ShowClient)

class ShowContact(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'message')
admin.site.register(Contact, ShowContact)

class ShowGuard(admin.ModelAdmin):
    list_display = ('image', 'name', 'status')
admin.site.register(Guard, ShowGuard)


