from django.shortcuts import redirect, render
from django.views.generic import CreateView
import logging
from django.views.generic import View 
from .models import Product, Product_Category
from django.contrib.auth.models import User
from django.http import Http404
from django.contrib.auth.models import  Permission,User
from django.contrib import messages
from django.http import HttpResponseRedirect
import json

def check_user_able_to_see_page(c_t):

    def decorator(function):
        def wrapper(request, *args, **kwargs):
            # if request.request.user.groups.filter(name=groups).exists():
            # permission = Permission.objects.get(codename=c_t)
            if request.request.user.has_perm("inventory."+c_t):
                print("demo")
                return function(request, *args, **kwargs)
            messages.error(request.request, f"You don't have Permission for this page")
            return HttpResponseRedirect(request.request.META.get('HTTP_REFERER'))

        return wrapper

    return decorator


logger = logging.getLogger(__name__)


class AddProductsCategory(CreateView):
    # model = Product_Category
    
    
    @check_user_able_to_see_page('view_product_category')
    def get(self, request, *args, **kwargs):
        all_category = Product_Category.objects.all()
        context ={
            'all_category': all_category
        }
        return render(request, 'category_list.html',context )

    @check_user_able_to_see_page('add_product_category')
    def post(self, request, *args, **kwargs):
        post_name = request.POST['category_name']
        Product_Category.objects.create(category_name=post_name)
        return redirect('add-category' )

class ViewProducts(View):

    @check_user_able_to_see_page('view_product')
    def get(self, request, *args, **kwargs):
        all_product = Product.objects.all()
        context ={
            'all_category': all_product
        }
        return render(request, 'product_list.html',context )


class AddProducts(CreateView):
    @check_user_able_to_see_page('add_product')
    def get(self, request, *args, **kwargs):
        all_category = Product_Category.objects.all()
        context ={
            'all_category': all_category
        }
        return render(request, 'add_product.html',context )

    @check_user_able_to_see_page('add_product')
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
    
class UpdateProduct(View):

    def get_object(self):
        try:
            ids = self.kwargs['id']
            print(ids)
            return Product.objects.get(Product_ID=ids)
        except Product.DoesNotExist:
            raise Http404

    # @check_user_able_to_see_page('add_machine')
    def get(self, request, *args, **kwargs):
        product = self.get_object()
        products = Product.objects.filter(Product_ID=self.kwargs['id'])
        all_category = Product_Category.objects.all()
        context ={
            'all_category': all_category,
            'product':product,
            'data': json.dumps(list(products.values()))
        }
        return render(request, 'add_product.html' ,context)

    # @check_user_able_to_see_page('add_machine')
    def post(self, request, *args, **kwargs):
        ids = self.kwargs['id']
        print(ids)
        categorie_instance = Product_Category.objects.get(category_ID=request.POST['categories'])
        product = Product.objects.get(Product_ID=ids)
        product.Product_Name = request.POST['product_name']
        product.category = categorie_instance
        product.Product_Stock = request.POST['status']
        product.image = request.FILES['user_img']
        product.available_quantity = request.POST['quantity']
        product.product_price = request.POST['product_price']
        product.save()
        return redirect('list-product')

from django.contrib.auth.models import Permission

def EditUserView(request,id=0):
    user = User.objects.get(pk=id)
    permission = Permission.objects.all()
    return render(request,'demo.html',{"userdata":user,"permissions":permission})