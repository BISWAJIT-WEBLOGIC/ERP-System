from django.contrib import admin
from django.urls import path ,include
from  .views import Home,LoginView,LogoutView,AddCategory,AddItem ,password_reset_request
from functools import wraps
from django.http import HttpResponseRedirect

# def anonymous_required(redirect_url=None):
#     """
#     Decorator that redirects authenticated users to a different URL.
#     """

#     def decorator(view_func):
#         @wraps(view_func, assigned=available_attrs(view_func))
#         def _wrapped_view(request, *args, **kwargs):
#             if request.user.is_anonymous():
#                 return view_func(request, *args, **kwargs)
#             return HttpResponseRedirect(redirect_url)
#         return _wrapped_view
#     return decorator



urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('add_category', AddCategory.as_view(), name='add-category'),
    path('add_item', AddItem.as_view(), name='add-item'),
    # path('wizard/', anonymous_required('login')(LoginView.as_view())),
    path("password_reset", password_reset_request, name="password_reset")
]
