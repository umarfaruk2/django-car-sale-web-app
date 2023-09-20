from django.shortcuts import render, redirect
from dashboard.models import AddProductModel
from .models import OrderModel
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from review_rating.models import ReviewRatingModel


def order_detail(request, id):
	data = AddProductModel.objects.get(pk = id) 
	review_and_rating = ReviewRatingModel.objects.filter(product = data)

	return render(request, 'order/order.html', {'data': data, 'review': review_and_rating})


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
