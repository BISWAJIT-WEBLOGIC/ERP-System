from django.contrib import admin
from django.urls import path ,include
from  .views import Home,LoginView,LogoutView,AddCategory,AddItem ,password_reset_request

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path("password_reset", password_reset_request, name="password_reset")
]
