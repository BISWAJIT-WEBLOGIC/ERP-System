from django.db import models
from adminpanel.customer.models import Customer
from adminpanel.inventory.models import Product
import random


# Create your models here.


class Order(models.Model):
    order_ID = models.BigAutoField( primary_key=True)
    order_code = models.CharField(max_length=255, unique=True,null=True,blank=True)
    customer = models.ForeignKey(Customer,  on_delete=models.CASCADE)
    product = models.ForeignKey(Product,  on_delete=models.CASCADE)
    quantity = models.CharField(max_length=255)
    price = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        random_no = random.randint(0,99999)
        self.order_code = random_no
        super(Order, self).save(*args, **kwargs)

