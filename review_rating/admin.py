from django.contrib import admin
from .models import ReviewRatingModel

@admin.register(ReviewRatingModel)
class ReviewRatingModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'review', 'rating')