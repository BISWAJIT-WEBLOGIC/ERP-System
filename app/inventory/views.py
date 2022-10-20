from multiprocessing import context
from django.shortcuts import redirect, render
from django.views.generic import CreateView
import logging
from django.views.generic import View 
from .models import Product, Product_Category


logger = logging.getLogger(__name__)


class AddProductsCategory(CreateView):
    def get(self, request, *args, **kwargs):
        all_category = Product_Category.objects.all()
        context ={
            'all_category': all_category
        }
        return render(request, 'list-item.html',context )

    def post(self, request, *args, **kwargs):
        post_name = request.POST['category_name']
        Product_Category.objects.create(category_name=post_name)
        return render(request, 'list-item.html' )

class AddProducts(CreateView):
    def get(self, request, *args, **kwargs):
        all_category = Product_Category.objects.all()
        # for category in all_category:
        #     print(all_category.id)
        context ={
            'all_category': all_category
        }
        return render(request, 'add-item.html',context )

    def post(self, request, *args, **kwargs):
        if request.FILES:
            post_name = request.POST['product_name']
            post_categories = request.POST['categories']
            post_status = request.POST['status']
            filename = request.FILES['user_img']
            categorie_instance = Product_Category.objects.get(category_ID=post_categories)
            Product.objects.create(Product_Name=post_name,category=categorie_instance, Product_Stock=post_status, image=filename)
            # print(post_categories,post_name,post_status,filename)
            return redirect('add-item' )
        print("nnnnnnnnnnnnnnnnnnnnn")
        return redirect('add-item' )