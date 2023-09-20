from django.db import models
from django.contrib.auth.models import User


class AddProductModel(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/product')

    def __str__(self):
        return self.title