from django.contrib import admin
from django.urls import path,include
from main import views 

urlpatterns = [

    
    path('',views.home,name='home'),
    path('services/',views.services,name='services'),
    path('contact/',views.contact,name='contact'),
    path('add_prod/',views.add_prod,name='add_prod'),
]
