from django.contrib import admin
from .models import AddProductModel

@admin.register(AddProductModel)
class AddProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'description', 'price')
    