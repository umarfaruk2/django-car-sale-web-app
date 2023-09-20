from django.urls import path
from . import views

urlpatterns = [
    path('add_product/', views.add_product, name='add_product'),
    path('my_order/', views.orderList, name='my_order'),
    path('product_manage/', views.product_list, name='product_manage'),
    path('update_product/<int:pk>', views.UpdateProduct.as_view(), name='update_product'),
    path('manage_order/', views.manage_order, name='manage_order'),
    path('delete_order/<int:id>', views.delete_order, name='delete_order'),
    path('order_status/<int:id>', views.order_status, name='order_status')
]