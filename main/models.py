from django.db import models
import os 

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100,blank=True,default="Name Not Mentioned")
    email = models.EmailField(max_length=122,blank=True,name="email@gmail.com")
    phone_number = models.IntegerField(blank=True,null=True)
    desc  = models.TextField(max_length=500,blank=True,null=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    sweets = "sweets"
    choclates = "choclates"
    junk_food = "Junk Food"

    choices= (
        (sweets,"sweets"),
        (choclates,"choclates"),
        (junk_food,"Junk Food")
    )




    prod_name = models.CharField(max_length=100,blank=True,default="PROD_NAME")
    prod_img = models.ImageField(upload_to="products/",blank=True,null=True)
    price = models.IntegerField(default=123)
    prod_desc = models.TextField(max_length=500,blank=True,default="No desc")
    category = models.CharField(max_length=10,choices=choices,default=sweets)


    def __str__(self):
        return self.prod_name 

