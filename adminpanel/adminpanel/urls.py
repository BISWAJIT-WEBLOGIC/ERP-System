from django.contrib import admin
from django.urls import path ,include
from  .views import Home,LoginView,LogoutView,AddCategory,AddItem ,password_reset_request
from adminpanel.inventory.views import AddProductsCategory ,AddProducts ,ViewProducts ,EditUserView
from adminpanel.machine.views import AddMachine , ListMachine
from adminpanel.account.views import ListUser , CreateUser
from adminpanel.customer.views import AddCustomer , ListCustomer


handler404 = 'adminpanel.adminpanel.views.page_not_found'

urlpatterns = [

    path('', Home.as_view(), name='home'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path("password_reset", password_reset_request, name="password_reset"),

         #..............account................

    path('list_user', ListUser.as_view(), name='list-user'),
    path('add_user', CreateUser.as_view(), name='add-user'),

    # ...............inventory....................
    path('add_category', AddProductsCategory.as_view(), name='add-category'),
    path('add_product', AddProducts.as_view(), name='add-product'),
    path('list_product', ViewProducts.as_view(), name='list-product'),
    path('demo/<id>/', EditUserView, name='demo'),

    #..............machine................

    path('add_machine', AddMachine.as_view(), name='add-machine'),
    path('list_machine', ListMachine.as_view(), name='list-machine'),

     #..............Customer................

    path('add_customer', AddCustomer.as_view(), name='add-customer'),
    path('list_customer', ListCustomer.as_view(), name='list-customer'),
]
