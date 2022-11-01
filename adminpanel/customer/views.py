from django.shortcuts import redirect, render
from django.views import View
from .models import Customer
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import Http404

def check_user_able_to_see_page(c_t):

    def decorator(function):
        def wrapper(request, *args, **kwargs):
            if request.request.user.has_perm("customer."+c_t):
                return function(request, *args, **kwargs)
            messages.error(request.request, f"You don't have Permission for this page")
            return HttpResponseRedirect(request.request.META.get('HTTP_REFERER'))

        return wrapper

    return decorator


class ListCustomer(View):
    @check_user_able_to_see_page('view_customer')
    def get(self, request, *args, **kwargs):
        all_customer = Customer.objects.all()
        print(all_customer)
        context ={
            'all_customer': all_customer
        }
        return render(request, 'customer_list.html',context )

class AddCustomer(View):
    
    @check_user_able_to_see_page('add_customer')
    def get(self, request, *args, **kwargs):
        return render(request, 'add_customer.html' )

    @check_user_able_to_see_page('add_customer')
    def post(self, request, *args, **kwargs):
        post_p_number = request.POST['p_number']
        if request.POST['p_number'] == '':
            post_p_number =None
        else:
            post_p_number = request.POST['p_number']
        
        post_name = request.POST['name']
        post_email = request.POST['email']
        post_t_p_amount = request.POST['t_p_amount']
        post_address = request.POST['address']
        Customer.objects.create(name=post_name,email=post_email,totalpurchaseamount=post_t_p_amount,
                                ph_number=post_p_number,address=post_address)
        return redirect('list-customer')
    
class UpdateCustomer(View):

    def get_object(self):
        try:
            ids = self.kwargs['id']
            print(ids)
            return Customer.objects.get(customer_Id=ids)
        except Customer.DoesNotExist:
            raise Http404

    # @check_user_able_to_see_page('add_machine')
    def get(self, request, *args, **kwargs):
        customer = self.get_object()
        print(customer)
        context ={
            'customer': customer
        }
        return render(request, 'add_customer.html' ,context)

    # @check_user_able_to_see_page('add_machine')
    def post(self, request, *args, **kwargs):
        customer = self.get_object()
        post_p_number = request.POST['p_number']
        if request.POST['p_number'] == '':
            post_p_number =None
        else:
            post_p_number = request.POST['p_number']
        
        customer.name = request.POST['name']
        customer.email = request.POST['email']
        customer.totalpurchaseamount = request.POST['t_p_amount']
        customer.ph_number = post_p_number
        customer.address = request.POST['address']
        customer.save()
        return redirect('list-customer')
