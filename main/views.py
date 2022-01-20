from django.shortcuts import render,HttpResponse
from .models import Contact,Product
from django.contrib import messages
import math

# Create your views here.


def home(request):
    products = Product.objects.all()

    return render(request,'home.html',{'pproducts':products})


def services(request):
    products = Product.objects.all()
    

    return render(request,'services.html',{"products":products})

def contact(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['no']
        desc = request.POST['desc']

        contact = Contact(name=name,email=email,phone_number=phone,desc=desc)
        contact.save()
        messages.success(request,'Your request has been submitted successfully')

    
    return render(request,'contacts.html')


def add_prod(request):
    if request.method=="POST":
        prod_name = request.POST['prod_name']
        prod_img = request.FILES['prod_img']
        prod_desc = request.POST['prod_desc']
        prod_rate = request.POST['prod_rate']
        cat = request.POST['cat']


        product = Product(prod_name=prod_name,prod_img=prod_img,prod_desc=prod_desc,category=cat,price=prod_rate)
        product.save()

        messages.success(request,"Your Product Has Been Added !")



    return render(request,'add_product.html')