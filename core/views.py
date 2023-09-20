from django.shortcuts import render
from dashboard.models import AddProductModel

def home(request):
    data = AddProductModel.objects.all()

    return render(request, 'index.html', {'data': data})