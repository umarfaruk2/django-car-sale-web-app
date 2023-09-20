from django import forms
from .models import AddProductModel


class AddProductModelForm(forms.ModelForm):
    class Meta:
        model = AddProductModel
        fields = ['title', 'description', 'price', 'image']