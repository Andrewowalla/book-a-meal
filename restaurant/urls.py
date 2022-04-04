from django.urls import path
from .views import Dashboard, OrderDetails


urlpattern = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('order/<int:pk>/', OrderDetails.as_view(), name='order-details'),
]

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),

]