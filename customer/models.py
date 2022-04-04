from ast import Delete

from django.db import models

class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    items = models.ForeignKey('MenuItem', related_name='order', blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    street = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zip_paid = models.IntegerField(blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    is_shipped = models.BooleanField(default=False)

    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'


    
import datetime as dt
# Create your models here.

class MenuItem(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    image =models.ImageField(upload_to='images/')
    price =models.DecimalField(max_digits=5,decimal_places=2)
    category=models.ForeignKey('Category', related_name='item', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add = True )
    price = models.DecimalField(max_digits=7, decimal_places=2)
    items=models.ForeignKey('MenuItem',related_name='order',blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    email=models.CharField(max_length=50, blank=True)
    street =models.CharField(max_length=50 , blank=True)
    city =models.CharField(max_length=50 , blank= True)
    is_paid = models.BooleanField(default=False)
    is_shipped = models.BooleanField(default=False)
    
    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'
