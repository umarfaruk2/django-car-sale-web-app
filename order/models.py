from django.db import models
from dashboard.models import AddProductModel
from django.contrib.auth.models import User


class OrderModel(models.Model):
	STATUS = (
        ('PENDING', 'PENDING'),
        ('PROCESS', 'PROCESS'),
        ('DELIVER', 'DELIVER'),
    )
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(AddProductModel, on_delete=models.CASCADE)
	status = models.CharField(choices=STATUS, default='PENDING', max_length=20)

	
