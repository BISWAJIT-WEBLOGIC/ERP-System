# from django.db import models

# STOCK_CHOICES = (
#     ("A", "Active"),
#     ("I", "Inactive")
# )

# # Create your models here.
# class Product(models.Model):
#     PRD_ID = models.BigAutoField("ProductID", primary_key=True)
#     PRD_NM = models.CharField("ProductName",max_length=255, )
#     stock = models.CharField(
#         "ProductStock", max_length=2, choices=STOCK_CHOICES, default="A")
#     image = models.ImageField("ProductSImage")
    
#     def __str__(self):
#         return self.PRD_NM