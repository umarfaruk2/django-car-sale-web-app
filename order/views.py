from django.shortcuts import render, redirect
from dashboard.models import AddProductModel
from .models import OrderModel
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


def order_detail(request, id):
	data = AddProductModel.objects.get(pk = id) 

	return render(request, 'order/order.html', {'data': data})


def order(request, id):
	if request.user.is_authenticated:
		product = AddProductModel.objects.get(pk = id)
		try:
			is_have_order = OrderModel.objects.get(product = product, user = request.user)
			return redirect('my_order')
		except ObjectDoesNotExist:	
			OrderModel.objects.create(product = product, user = request.user)

		return redirect('home') 
	else:
		return redirect('login')



    
