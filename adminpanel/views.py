# Create your views here.
from django.shortcuts import render , redirect
from django.views.generic import View ,ListView
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render 
from django.template import RequestContext ,loader
from django.http import HttpResponseNotFound





def page_not_found(request, exception):
    content = loader.render_to_string('404.html', {}, request)
    return HttpResponseNotFound(content)

class Home(View):
    # template_name = 'index.html'
    
    @method_decorator(login_required())
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")
    
class AddCategory(View):
    def get(self, request, *args, **kwargs):
        return render(request, "list-item.html")
    
class AddItem(View):
    def get(self, request, *args, **kwargs):
        return render(request, "add-item.html")

from django.views.decorators.cache import never_cache


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, "login.html")
        else:
            return redirect('home')
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = authenticate(username=username, password=password)
        except:
            user = User.objects.filter(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
        else:
            return render(request, "login.html")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')