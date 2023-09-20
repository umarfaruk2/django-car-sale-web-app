from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from order.models import OrderModel
from .forms import AddProductModelForm
from .models import AddProductModel
from django.views.generic.edit import UpdateView
from .forms import AddProductModelForm

def my_order(request):
    return render(request, 'dashboard/my_order.html')

def add_product(request):
    if request.method == 'POST':
        fm = AddProductModelForm(request.POST, request.FILES)        
        if fm.is_valid():
            fm.instance.user = request.user
            fm.save()
            return redirect('add_product')
    else:
        fm = AddProductModelForm()
    return render(request, 'dashboard/add_product.html', {'form': fm})


def orderList(request):
    my_order = OrderModel.objects.filter(user = request.user)
    return render(request, 'dashboard/my_order.html', {'data': my_order})

def manage_order(request):
    orders = OrderModel.objects.all()
    return render(request, 'dashboard/manage_order.html', {'data': orders})


def product_list(request):
    product = AddProductModel.objects.all()
    return render(request, 'dashboard/product_list.html', {'data': product})

class UpdateProduct(UpdateView):
    template_name = 'dashboard/update_product.html' 
    model = AddProductModel
    form_class = AddProductModelForm
    success_url = reverse_lazy('product_manage') 

def delete_order(request, id):
    OrderModel.objects.get(pk = id).delete() 
    return redirect('manage_order')

def order_status(request, id):
    if request.method == 'POST':
        option = request.POST.get('selected_option')
        print(option)
        order = OrderModel.objects.get(pk = id)
        print(order)
        if option == 'PENDING':
           order.status = option 
        elif option == 'PROCESS':
            order.status = option
        elif option == 'DELIVER':
            order.status = option
        
        order.save()
            
        return redirect('manage_order')


    