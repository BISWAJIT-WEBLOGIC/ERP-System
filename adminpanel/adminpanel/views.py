# Create your views here.
from django.shortcuts import render , redirect
from django.views.generic import View 
from django.contrib.auth import authenticate , login ,logout
from adminpanel.account.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render 
from django.template import loader
from django.http import HttpResponseNotFound ,HttpResponse
from django.views.decorators.cache import never_cache
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.conf import settings
from django.contrib import messages





def page_not_found(request, exception):
    content = loader.render_to_string('404.html', {}, request)
    return HttpResponseNotFound(content)

class Home(View):
    
    @method_decorator(login_required())
    def get(self, request, *args, **kwargs):
        request.user.has_perm('machine.change_machine', obj=None)
        return render(request, "index.html")
    
# class AddCategory(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, "list-item.html")
    
# class AddItem(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, "add-item.html")


class LoginView(View):
    @method_decorator(never_cache)
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, "login.html")
        else:
            return redirect('home')
    
    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = authenticate(email=email, password=password)
        except:
            user = User.objects.filter(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, f'You are login as using {request.user}')
                return redirect('home')
        else:
            messages.error(request, 'Please enter valid email and password')
            return render(request, "login.html")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        # print(request.environ['HTTP_HOST'])
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password_reset_email.txt"
                    c = {
					"email":user.email,
					'domain':request.environ['HTTP_HOST'],
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
                    
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, str(settings.EMAIL_HOST_USER[0]) , [data], fail_silently=False)
                        messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
                        return redirect ('login')
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
            messages.error(request, 'An invalid email has been entered.')
            return redirect ('password_reset')


    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password_reset.html", context={"password_reset_form":password_reset_form})