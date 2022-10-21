from. views import AddMachine , ListMachine
from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


handler404 = 'adminpanel.views.page_not_found'
urlpatterns = [
    path('add_machine', AddMachine.as_view(), name='add-machine'),
    path('list_machine', ListMachine.as_view(), name='list-machine'),
] 