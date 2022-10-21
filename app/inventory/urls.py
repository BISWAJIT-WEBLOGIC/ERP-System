from. views import AddProductsCategory ,AddProducts ,ViewProducts ,EditUserView
from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 


handler404 = 'adminpanel.views.page_not_found'
urlpatterns = [
    path('add_category', AddProductsCategory.as_view(), name='add-category'),
    path('add_product', AddProducts.as_view(), name='add-product'),
    path('list_product', ViewProducts.as_view(), name='list-product'),
    path('demo/<id>/', EditUserView, name='demo'),
] 
