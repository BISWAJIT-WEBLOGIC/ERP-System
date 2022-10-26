from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views #import this
from django.urls import reverse_lazy


handler404 = 'adminpanel.adminpanel.views.page_not_found'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminpanel/', include('adminpanel.adminpanel.urls')),
#     path('inventory/', include('adminpanel.inventory.urls')),
#     path('machine/', include('adminpanel.machine.urls')), 
    path('api/', include('api.login_authentication.urls')),
    # path('', include('user.urls')),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html")
                                                                                 , name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
] 

      # serve  static file
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

      # serve media file
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

