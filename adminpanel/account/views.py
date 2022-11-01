from multiprocessing import context
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from .models import User
from django.db.models.query_utils import Q
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Permission
from .form import UserGroupForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import Http404

def check_user_able_to_see_page(c_t):

    def decorator(function):
        def wrapper(request, *args, **kwargs):
            if request.request.user.has_perm("account."+c_t):
                return function(request, *args, **kwargs)
            messages.error(request.request, f"You don't have Permission for this page")
            return HttpResponseRedirect(request.request.META.get('HTTP_REFERER'))

        return wrapper

    return decorator


def permission_string_method(self):
    return '%s' % (self.name)
Permission.__str__ = permission_string_method

# Permission.__str__ = lambda self: '%s' % (self.name)


class ListUser(View):

    @method_decorator(login_required())
    @check_user_able_to_see_page('view_user')
    def get(self, request, *args, **kwargs):
        users =User.objects.all()
        context = {
            'users':users,
        }
        return render(request, "user_list.html",context)
    

class CreateUser(View):

    @method_decorator(login_required())
    @check_user_able_to_see_page('add_user')
    def get(self, request, *args, **kwargs):
            group =Group.objects.all()
            context ={
                'group':group
            }
            return render(request, "add_user.html",context)
    
    @method_decorator(login_required())
    @check_user_able_to_see_page('add_user')
    def post(self, request):
        post_group = request.POST['group']
        group = Group.objects.get(name=post_group)
        if request.POST['p_number'] == '':
            ph_n =None
        else:
            ph_n = request.POST['p_number']
        if User.objects.filter(Q(email=request.POST['email'])).exists(): 
            messages.info(request, "Email-is all redy exits" )
            return redirect('add-user') 
        else:
            user =User.objects.create(first_name=request.POST['f_name'],
                                last_name=request.POST['l_name'],
                                email=request.POST['email'],
                                ph_number=ph_n,
                                address=request.POST['address'],
                                designation=group.name)
            user.set_password(request.POST['password'])
            user.groups.add(group)
            user.save()
            messages.info(request, "User create successfully" )
            return redirect('list-user')


class CreateGroup(View):
    

    @method_decorator(login_required())
    # @check_user_able_to_see_page('add_user')
    def get(self, request, *args, **kwargs):
        form = UserGroupForm()
        group = Group.objects.all()
        print(group.__dict__)
        context = {
        'form': form,
        'group':group
        }
        return render(request,'add_permitions_group.html',context)

    @method_decorator(login_required())
    # @check_user_able_to_see_page('add_user')
    def post(self, request):
        form = UserGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create-group')
        else:
            forms = UserGroupForm()
            group = Group.objects.all()
            error = form.errors
            error =list(error.as_data()["name"][0])
            context = {
            'form': forms,
            # 'error':error[0],
            'group':group
            }
            messages.error(request, error[0])
            return render(request,'add_permitions_group.html',context)
        
class UpdateUser(View):

    def get_object(self):
        try:
            ids = self.kwargs['id']
            print(ids)
            return User.objects.get(id=ids)
        except User.DoesNotExist:
            raise Http404

    # @check_user_able_to_see_page('add_machine')
    def get(self, request, *args, **kwargs):
        user = self.get_object()
        group =Group.objects.all()
        context ={
            'group':group,
            'user': user
        }
        return render(request, 'add_user.html' ,context)

    # @check_user_able_to_see_page('add_machine')
    def post(self, request, *args, **kwargs):
        post_group = request.POST['group']
        group = Group.objects.get(name=post_group)
        if request.POST['p_number'] == '':
            ph_n =None
        else:
            ph_n = request.POST['p_number']

        user = self.get_object()

        if User.objects.filter(Q(email=request.POST['email'])) == user.email:
            messages.info(request, "Email-is all redy exits" )
            return redirect('add-user') 
        else:
            user.first_name=request.POST['f_name']
            user.last_name=request.POST['l_name']
            user.email=request.POST['email']
            user.ph_number=ph_n
            user.address=request.POST['address'],
            # designation=group.name)
            user.save()
            return redirect('list-user')