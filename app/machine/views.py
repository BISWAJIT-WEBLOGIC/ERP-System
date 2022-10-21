from django.shortcuts import redirect, render
from django.views import View
from .models import Machine

# Create your views here.


class ListMachine(View):
    def get(self, request, *args, **kwargs):
        all_machine = Machine.objects.all()
        print(all_machine)
        context ={
            'all_machine': all_machine
        }
        return render(request, 'machine_list.html',context )

class AddMachine(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'add_machine.html' )

    def post(self, request, *args, **kwargs):
        post_name = request.POST['machine_name']
        post_machine_temp = request.POST['machine_temp']
        post_registration_no = request.POST['registration_no']
        Machine.objects.create(machine_name=post_name,machine_current_temperature=post_machine_temp,machine_registration_no=post_registration_no)
        return redirect('list-machine')
