from django.db import models
from dashboard.models import AddProductModel

class ReviewRatingModel(models.Model):
    RATING_VALUE = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    product = models.ForeignKey(AddProductModel, on_delete=models.CASCADE, default=None) 
    review = models.TextField(max_length=100)
    rating = models.IntegerField(choices=RATING_VALUE)

    

