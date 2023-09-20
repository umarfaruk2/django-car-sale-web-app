from django.urls import path
from . import views

urlpatterns = [
    path('order_detail/<int:id>', views.order_detail, name='order_detail'),
    path('order/<int:id>', views.order, name='order'),
]
