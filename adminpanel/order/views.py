from django.shortcuts import redirect, render
from django.views import View
from .models import Order
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from adminpanel.customer.models import Customer
from adminpanel.inventory.models import Product
import json

def check_user_able_to_see_page(c_t):

    def decorator(function):
        def wrapper(request, *args, **kwargs):
            # if request.request.user.groups.filter(name=groups).exists():
            # permission = Permission.objects.get(codename=c_t)
            if request.request.user.has_perm("Order."+c_t):
                return function(request, *args, **kwargs)
            messages.error(request.request, f"You don't have Permission for this page")
            return HttpResponseRedirect(request.request.META.get('HTTP_REFERER'))

        return wrapper

    return decorator


class ListOrder(View):

    @method_decorator(login_required())
    @check_user_able_to_see_page('view_order')
    def get(self, request, *args, **kwargs):
        all_order = Order.objects.all()
        post_product = Product.objects.get(Product_ID=2)
        context ={
            'all_order': all_order
        }
        return render(request, 'order_list.html',context )

class AddOrder(View):

    @method_decorator(login_required())
    @check_user_able_to_see_page('add_order')
    def get(self, request, *args, **kwargs):
        product = Product.objects.all()
        customer = Customer.objects.all()
        context ={
            'all_product':product,
            'all_customer':customer
        }
        return render(request, 'add_order.html',context)

    @method_decorator(login_required())
    @check_user_able_to_see_page('add_order')
    def post(self, request, *args, **kwargs):
        post_product = request.POST['product']
        post_customer = request.POST['customer']
        post_quantity = request.POST['quantity']
        post_price = request.POST['price']
        post_customer = Customer.objects.get(customer_Id=post_customer)
        post_product = Product.objects.get(Product_ID=post_product)
        Order.objects.create(customer=post_customer,product=post_product,quantity=post_quantity,price=post_price)
        return redirect('list-order')


class UpdateOrder(View):

    def get_object(self):
        try:
            ids = self.kwargs['id']
            return Order.objects.get(order_ID=ids)
        except Order.DoesNotExist:
            raise Http404

    @method_decorator(login_required())
    @check_user_able_to_see_page('change_order')
    def get(self, request, *args, **kwargs):
        order = self.get_object()
        product = Product.objects.all()
        customer = Customer.objects.all()
        orders = Order.objects.filter(order_ID=self.kwargs['id'])
        context ={
            'all_product':product,
            'all_customer':customer,
            'order': order,
            'data': json.dumps(list(orders.values()))
        }
        return render(request, 'add_order.html' ,context)

    @method_decorator(login_required())
    @check_user_able_to_see_page('change_order')
    def post(self, request, *args, **kwargs):
        order = Order.objects.filter(order_ID=kwargs['id'])
        post_product = request.POST['product']
        post_customer = request.POST['customer']
        post_customer = Customer.objects.get(customer_Id=post_customer)
        post_product = Product.objects.get(Product_ID=post_product)
        order.update(customer=post_customer,
                    product=post_product,
                    quantity=request.POST['quantity'],
                    price=request.POST['price'])
        return redirect('list-order')