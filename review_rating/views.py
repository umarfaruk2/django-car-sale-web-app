from django.shortcuts import render, redirect
from .forms import ReviewRatingForm
from order.models import OrderModel
from dashboard.models import AddProductModel
from django.contrib import messages


def review_rating(request, id):
    if request.user.is_authenticated:
        product = AddProductModel.objects.get(pk = id)
        try:
            is_have_order = OrderModel.objects.get(product = product, user = request.user) 

            if request.method == 'POST':
                fm = ReviewRatingForm(request.POST)
                if fm.is_valid():
                    fm.instance.product = product
                    fm.save()
                    return redirect('order_detail', id = id)
            else:
                fm =  ReviewRatingForm()
            return render(request, 'review_rating/review_rating.html', {'form': fm})
        except:
            messages.error(request, "Not found in order list, so you can't review for this product!")
            return redirect('order_detail', id = id)
            
    else:
        return redirect('login') 