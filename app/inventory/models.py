from django.db import models
from django.conf import settings

STOCK_CHOICES = (
    ("A", "Active"),
    ("I", "Inactive")
)

class Product_Category(models.Model):
    category_ID = models.BigAutoField( primary_key=True)
    category_name = models.CharField(max_length=255 )
    
    def __str__(self):
        return self.category_name

# Create your models here.
class Product(models.Model):
    Product_ID = models.BigAutoField( primary_key=True)
    Product_Name = models.CharField(max_length=255 )
    available_quantity = models.CharField(max_length=255)
    product_price= models.CharField(max_length=255 )
    category = models.ForeignKey(Product_Category,null=True, blank=True,on_delete=models.CASCADE)
    Product_Stock = models.CharField(
         max_length=2, choices=STOCK_CHOICES, default="A")
    image = models.ImageField("Product Image",upload_to='inventory')
    
    def __str__(self):
        return self.Product_Name

