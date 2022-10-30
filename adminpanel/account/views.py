from multiprocessing import context
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from .models import User
from django.db.models.query_utils import Q
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from .form import UserGroupForm

def permission_string_method(self):
    return '%s' % (self.name)
Permission.__str__ = permission_string_method

# Permission.__str__ = lambda self: '%s' % (self.name)


class ListUser(View):
    def get(self, request, *args, **kwargs):
        if request.user.has_perm('aaa'):
            print(request.user)
            user =User.objects.all()
            context = {
                'users':user
            }
            return render(request, "user_list.html",context)

class CreateUser(View):
    # @method_decorator(never_cache)
    def get(self, request, *args, **kwargs):
            print("MMMMMMMMMMMMMMMMMMM")
            group =Group.objects.all()
            context ={
                'group':group
            }
            return render(request, "add_user.html",context)
    
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


def create_group(request):
    error = None
    if request.method == 'POST':
        form = UserGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create-group')
        else:
            forms = UserGroupForm()
            group = Group.objects.all()
            error = form.errors
            context = {
            'form': forms,
            'error':error,
            'group':group
            }
            return render(request,'add_permitions_group.html',context)
    else:
        form = UserGroupForm()
        group = Group.objects.all()
        # user = User.objects.all()
        print(group.__dict__)
        # print(form)
        context = {
        'form': form,
        'group':group
        }
        return render(request,'add_permitions_group.html',context)