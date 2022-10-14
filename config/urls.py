from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static


handler404 = 'adminpanel.views.page_not_found'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminpanel/', include('adminpanel.urls')),
    path('api/', include('api.login_authentication.urls')),
    # path('', include('user.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
