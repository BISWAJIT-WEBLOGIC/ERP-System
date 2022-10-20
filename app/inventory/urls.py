from. views import AddProductsCategory ,AddProducts
from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


handler404 = 'adminpanel.views.page_not_found'
urlpatterns = [
    path('add_category', AddProductsCategory.as_view(), name='add-category'),
    path('add_item', AddProducts.as_view(), name='add-item'),
] 
