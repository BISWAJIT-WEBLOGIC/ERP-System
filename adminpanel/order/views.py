import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from adminpanel.customer.models import Customer
from adminpanel.inventory.models import Product

from .models import Order


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

        post_product_obj = Product.objects.get(Product_ID=post_product)
        if int(post_product_obj.available_quantity) >= int(post_quantity):

            product_price =post_product_obj.product_price
            total_price = (int(product_price)*int(post_quantity))

            post_customer = Customer.objects.get(customer_Id=post_customer)
            product_obj = Product.objects.filter(Product_ID=post_product)

            product_available_quantity =post_product_obj.available_quantity
            total_available_quantity = int(product_available_quantity)-int(post_quantity)

            product_obj.update(available_quantity=total_available_quantity)
            Order.objects.create(customer=post_customer,product=post_product_obj,
                                quantity=post_quantity,price=total_price)
            return redirect('list-order')
        
        messages.error(request, f'''Chack selected Product Stack, because your selected product " {post_product_obj.Product_Name} " have " {post_product_obj.available_quantity} " in stack''')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


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
        products = Product.objects.all()
        customer = Customer.objects.all()
        orders = Order.objects.filter(order_ID=self.kwargs['id'])
        product = Product.objects.filter(Product_ID=order.product.Product_ID)
        context ={
            'all_product':products,
            'all_customer':customer,
            'order': order,
            'orders_data': json.dumps(list(orders.values())),
            'product_data': json.dumps(list(product.values()))
        }
        return render(request, 'add_order.html' ,context)

    @method_decorator(login_required())
    @check_user_able_to_see_page('change_order')
    def post(self, request, *args, **kwargs):
        post_quantity =request.POST['quantity']
        post_products = request.POST['product']
        post_customer = request.POST['customer']
        post_status =request.POST['status']

        post_customer = Customer.objects.get(customer_Id=post_customer)
        post_product = Product.objects.get(Product_ID=post_products)
        print(post_product)
        order = Order.objects.get(order_ID=kwargs['id'])
        
        if int(post_product.available_quantity) >= int(post_quantity):
            print("1")
            if (int(order.quantity) > int(post_quantity)):
                print("2")
                discrise_order_quantity = (int(order.quantity) - int(post_quantity))
                final_product_quantity = int(post_product.available_quantity)+discrise_order_quantity
                final_order_price = int(order.price) - (int(post_product.product_price)*discrise_order_quantity)

                product_obj = Product.objects.filter(Product_ID=post_products)
                product_obj.update(available_quantity=final_product_quantity)

                order_obj = Order.objects.filter(order_ID=kwargs['id'])
                order_obj.update(customer=post_customer,
                            product=post_product,
                            quantity=post_quantity,
                            price=final_order_price,
                            status=post_status)
                return redirect('list-order')

            if (int(order.quantity) == int(post_quantity)):
                print("3")
                discrise_order_quantity = (int(order.quantity) - int(post_quantity))
                final_product_quantity = int(post_product.available_quantity)+discrise_order_quantity
                final_order_price = int(order.price) - (int(post_product.product_price)*discrise_order_quantity)

                product_obj = Product.objects.filter(Product_ID=post_products)
                product_obj.update(available_quantity=final_product_quantity)

                order_obj = Order.objects.filter(order_ID=kwargs['id'])
                order_obj.update(customer=post_customer,
                            product=post_product,
                            status=post_status)
                return redirect('list-order')

            if (int(order.quantity) < int(post_quantity)):
                print("4")
                discrise_order_quantity = (int(post_quantity) - int(order.quantity))
                final_product_quantity = int(post_product.available_quantity)-discrise_order_quantity
                final_order_price = int(order.price) + (int(post_product.product_price)*discrise_order_quantity)
                
                product_obj = Product.objects.filter(Product_ID=post_products)
                product_obj.update(available_quantity=final_product_quantity)

                order_obj = Order.objects.filter(order_ID=kwargs['id'])
                order_obj.update(customer=post_customer,
                            product=post_product,
                            quantity=post_quantity,
                            price=final_order_price,
                            status=post_status)
                return redirect('list-order')

        if int(post_product.available_quantity) <= int(post_quantity):
            print("5")
            if (int(order.quantity) > int(post_quantity)):
                print("6")
                discrise_order_quantity = (int(order.quantity) - int(post_quantity))
                final_product_quantity = int(post_product.available_quantity)+discrise_order_quantity
                final_order_price = int(order.price) - (int(post_product.product_price)*discrise_order_quantity)

                product_obj = Product.objects.filter(Product_ID=post_products)
                product_obj.update(available_quantity=final_product_quantity)

                order_obj = Order.objects.filter(order_ID=kwargs['id'])
                order_obj.update(customer=post_customer,
                            product=post_product,
                            quantity=post_quantity,
                            price=final_order_price,
                            status=post_status)
                return redirect('list-order')

            if (int(order.quantity) == int(post_quantity)):
                print("3")
                discrise_order_quantity = (int(order.quantity) - int(post_quantity))
                final_product_quantity = int(post_product.available_quantity)+discrise_order_quantity
                final_order_price = int(order.price) - (int(post_product.product_price)*discrise_order_quantity)

                product_obj = Product.objects.filter(Product_ID=post_products)
                product_obj.update(available_quantity=final_product_quantity)

                order_obj = Order.objects.filter(order_ID=kwargs['id'])
                order_obj.update(customer=post_customer,
                            product=post_product,
                            status=post_status)
                return redirect('list-order')
            
            if (int(order.quantity) < int(post_quantity)):
                discrise_order_quantity = (int(post_quantity) - int(order.quantity))
                print("7")
                if int(post_product.available_quantity) > 0:
                    final_product_quantity = int(post_product.available_quantity)-discrise_order_quantity
                    final_order_price = int(order.price) + (int(post_product.product_price)*discrise_order_quantity)
                    
                    product_obj = Product.objects.filter(Product_ID=post_products)
                    product_obj.update(available_quantity=final_product_quantity)

                    order_obj = Order.objects.filter(order_ID=kwargs['id'])
                    order_obj.update(customer=post_customer,
                                product=post_product,
                                quantity=post_quantity,
                                price=final_order_price,
                                status=post_status)
                    return redirect('list-order')

                messages.error(request, f"Chack selected Product Stack, because your selected product '{post_product.Product_Name}' have '{post_product.available_quantity}' in stack")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                

        messages.error(request, f"Chack selected Product Stack, because your selected product '{post_product.Product_Name}' have '{post_product.available_quantity}' in stack")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        