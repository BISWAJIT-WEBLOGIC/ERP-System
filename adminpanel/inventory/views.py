from multiprocessing import context
from django.shortcuts import redirect, render
from django.views.generic import CreateView
import logging
from django.views.generic import View 
from .models import Product, Product_Category
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import  Permission,User
from django.contrib.contenttypes.models import ContentType
from django.http import Http404

def check_user_able_to_see_page(groups,c_t):

    def decorator(function):
        def wrapper(request, *args, **kwargs):
            if request.request.user.groups.filter(name=groups).exists():
                permission = Permission.objects.get(codename=c_t)
                if Group.objects.filter(permissions=permission).exists():
                    return function(request, *args, **kwargs)
            raise Http404

        return wrapper

    return decorator


logger = logging.getLogger(__name__)


class AddProductsCategory(CreateView):
    model = Product_Category
    
    
    @check_user_able_to_see_page('demo','view_product_category')
    def get(self, request, *args, **kwargs):
        all_category = Product_Category.objects.all()
        context ={
            'all_category': all_category
        }
        return render(request, 'category_list.html',context )

    @check_user_able_to_see_page('demo','add_product_category')
    def post(self, request, *args, **kwargs):
        post_name = request.POST['category_name']
        Product_Category.objects.create(category_name=post_name)
        return redirect('add-category' )

class ViewProducts(View):

    @check_user_able_to_see_page('demo','view_product')
    def get(self, request, *args, **kwargs):
        all_product = Product.objects.all()
        context ={
            'all_category': all_product
        }
        return render(request, 'product_list.html',context )


class AddProducts(CreateView):
    @check_user_able_to_see_page('demo','add_product')
    def get(self, request, *args, **kwargs):
        all_category = Product_Category.objects.all()
        context ={
            'all_category': all_category
        }
        return render(request, 'add_product.html',context )

    @check_user_able_to_see_page('demo','add_product')
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