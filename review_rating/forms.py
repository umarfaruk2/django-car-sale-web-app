from django import forms
from .models import ReviewRatingModel



class ReviewRatingForm(forms.ModelForm):
    class Meta:
        model = ReviewRatingModel
        fields = ['review', 'rating']