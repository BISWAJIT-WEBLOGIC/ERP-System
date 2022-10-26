from django.db import models


class Customer(models.Model):
    customer_Id = models.BigAutoField( primary_key=True)
    name = models.CharField(max_length=255,)
    email = models.EmailField(max_length=255, )
    totalpurchaseamount = models.IntegerField(default=0,blank=True, null=True)
    ph_number = models.IntegerField( blank=True, null=True,default=None)
    address = models.TextField( blank=True, null=True)
    
    
    def __str__(self):
        return self.name
    