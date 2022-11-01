from django.shortcuts import redirect, render
from django.views import View
from .models import Machine
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import Http404

def check_user_able_to_see_page(c_t):

    def decorator(function):
        def wrapper(request, *args, **kwargs):
            # if request.request.user.groups.filter(name=groups).exists():
            # permission = Permission.objects.get(codename=c_t)
            if request.request.user.has_perm("machine."+c_t):
                return function(request, *args, **kwargs)
            messages.error(request.request, f"You don't have Permission for this page")
            return HttpResponseRedirect(request.request.META.get('HTTP_REFERER'))

        return wrapper

    return decorator


class ListMachine(View):

    @check_user_able_to_see_page('view_machine')
    def get(self, request, *args, **kwargs):
        all_machine = Machine.objects.all()
        print(all_machine)
        context ={
            'all_machine': all_machine
        }
        return render(request, 'machine_list.html',context )

class AddMachine(View):

    @check_user_able_to_see_page('add_machine')
    def get(self, request, *args, **kwargs):
        return render(request, 'add_machine.html' )

    @check_user_able_to_see_page('add_machine')
    def post(self, request, *args, **kwargs):
        post_name = request.POST['machine_name']
        post_machine_temp = request.POST['machine_temp']
        post_registration_no = request.POST['registration_no']
        Machine.objects.create(machine_name=post_name,machine_current_temperature=post_machine_temp,machine_registration_no=post_registration_no)
        return redirect('list-machine')


class UpdateMachine(View):

    def get_object(self):
        try:
            ids = self.kwargs['id']
            print(ids)
            return Machine.objects.get(machine_ID=ids)
        except Machine.DoesNotExist:
            raise Http404

    # @check_user_able_to_see_page('add_machine')
    def get(self, request, *args, **kwargs):
        machine = self.get_object()
        print(machine)
        context ={
            'machine': machine
        }
        return render(request, 'add_machine.html' ,context)

    # @check_user_able_to_see_page('add_machine')
    def post(self, request, *args, **kwargs):
        machine = self.get_object()
        machine.machine_name = request.POST['machine_name']
        machine.machine_current_temperature = request.POST['machine_temp']
        machine.machine_registration_no = request.POST['registration_no']
        machine.save()
        return redirect('list-machine')