from django.shortcuts import redirect, render
from django.views import View
from .models import Customer

# Create your views here.


class ListCustomer(View):
    def get(self, request, *args, **kwargs):
        all_customer = Customer.objects.all()
        print(all_customer)
        context ={
            'all_customer': all_customer
        }
        return render(request, 'customer_list.html',context )

class AddCustomer(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'add_customer.html' )

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
