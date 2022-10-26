from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from .models import User
from django.db.models.query_utils import Q

# Create your views here.

class ListUser(View):
    def get(self, request, *args, **kwargs):
        user =User.objects.all()
        context = {
            'users':user
        }
        return render(request, "user_list.html",context)

class CreateUser(View):
    # @method_decorator(never_cache)
    def get(self, request, *args, **kwargs):
        return render(request, "add_user.html")
    
    def post(self, request):
        password = request.POST['password']
        r_password = request.POST['re_password']
        if request.POST['p_number'] == '':
            ph_n =None
        else:
            ph_n = request.POST['p_number']

        if User.objects.filter(Q(email=request.POST['email'])).exists(): 
            messages.info(request, "Email-is all redy exits" )
            return redirect('add-user') 
        if password != r_password: 
            messages.info(request, "Enter same password in Confirm Password filed" )
            return redirect('add-user') 
        else:
            # print("demo")
            user =User.objects.create(first_name=request.POST['f_name'],
                                last_name=request.POST['l_name'],
                                email=request.POST['email'],
                                ph_number=ph_n,
                                address=request.POST['address'])
            user.set_password(request.POST['password'])
            user.save()
            messages.info(request, "User create successfully" )
            return redirect('list-user') 