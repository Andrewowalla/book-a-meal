from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')

class Order(View):
    def get(self,request, *args, **kwargs):
        
        #get each item from each category
        appetizers = MenuItem.objects.filter(category__name__contains = 'Appetizer')
        entres = MenuItem.objects.filter(category__name__contains = 'Entre')
        desserts = MenuItem.objects.filter(category__name__contains = 'Dessert')
        drinks = MenuItem.objects.filter(category__name__contains = 'Drink')

        #pass into context
        context = {
            'appetizers': appetizers,
            'entres':entres,
            'desserts':desserts,
            'drinks':drinks
        }
        #render the template
        return render(request,'customer/order.html',context)

def post (self,request, *args, **kwargs):
    order_items = {
        'items':[]
    }
    items = request.POST.getlist('items[]')
