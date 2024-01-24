from django.urls import path
from .views import  index, about, service, guard, contact

urlpatterns = [
    path("", index,  name='index'),
    path('front/about', about, name ='about' ),
    path('front/service', service, name ='service' ),
    path('front/guard', guard, name ='guard' ),
    path('front/contact', contact, name ='contact' ),
]