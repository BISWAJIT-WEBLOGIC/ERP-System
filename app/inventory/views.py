from multiprocessing import context
from django.shortcuts import redirect, render
from django.views.generic import CreateView
import logging
from django.views.generic import View 
from .models import Product, Product_Category
from django.contrib.auth.models import User


logger = logging.getLogger(__name__)


class AddProductsCategory(CreateView):
    def get(self, request, *args, **kwargs):
        all_category = Product_Category.objects.all()
        context ={
            'all_category': all_category
        }
        return render(request, 'category_list.html',context )

    def post(self, request, *args, **kwargs):
        post_name = request.POST['category_name']
        Product_Category.objects.create(category_name=post_name)
        return redirect('add-category' )

class ViewProducts(View):
    def get(self, request, *args, **kwargs):
        all_product = Product.objects.all()
        context ={
            'all_category': all_product
        }
        return render(request, 'product_list.html',context )


class AddProducts(CreateView):
    def get(self, request, *args, **kwargs):
        all_category = Product_Category.objects.all()
        context ={
            'all_category': all_category
        }
        return render(request, 'add_product.html',context )

    def post(self, request, *args, **kwargs):
        if request.FILES:
            post_name = request.POST['product_name']
            post_categories = request.POST['categories']
            post_status = request.POST['status']
            filename = request.FILES['user_img']
            post_quantity = request.POST['quantity']
            post_price = request.POST['product_price']
            categorie_instance = Product_Category.objects.get(category_ID=post_categories)
            Product.objects.create(Product_Name=post_name,category=categorie_instance, Product_Stock=post_status,
                                    image=filename,available_quantity=post_quantity,product_price=post_price )
            return redirect('list-product' )
        print("nnnnnnnnnnnnnnnnnnnnn")
        return redirect('add-product' )

from django.contrib.auth.models import Permission

def EditUserView(request,id=0):
    user = User.objects.get(pk=id)
    permission = Permission.objects.all()
    return render(request,'demo.html',{"userdata":user,"permissions":permission})