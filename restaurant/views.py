from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from customer.models import OrderModel
# Create your views here.

class OrderDetails(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, pk, *args, **kwargs):
        orde = OrderModel.objects.get(pk=pk)
        
    def test_func(self):
        return self.request.user.groups.filter(name='staff').exists()


