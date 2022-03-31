from django.shortcuts import render
from django.views import View
from django.db.models import Q
from .models import MenuItem
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')

class Menu(View):
    def get(self, request, *args, **kwargs):
        menu_items = MenuItem.objects.all()

        context = {
            'menu-items': menu-items
        }

        return render(request, 'customer/menu.html', context)

class MenuSearch(View):
    def get(self,  request, *args, **kwargs):
        query = self.request.GET.get("q")

        menu_items = MenuItem.object.filter(
            Q(name__icontains=query) |
            Q(price__icontains=query) |
            Q(description__icontains=query)
        ) 

        context = {
            'menu_items': menu_items
        }

        return render(request, 'customer/menu.html', context)        
        
