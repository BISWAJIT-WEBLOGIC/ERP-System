from django.urls import path
from api.login_authentication.views import  Logout, SignUp, Login
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)


class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    '''swagger scheme generator'''

    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["https", "http"]
        return schema


SchemaView = get_schema_view(
    openapi.Info(
        title="D&B Supply Api List",
        default_version='v1',
        description="Api description",
        terms_of_service="https://www.dnb.com",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="Tset License"),
    ),
    public=True,
    generator_class=BothHttpAndHttpsSchemaGenerator,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('', SchemaView.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    path('signin/', Login.as_view(), name='api-signin'),
    path('signup/', SignUp.as_view(), name='api-signup'),
    path('logout/', Logout.as_view(), name='api-logout')
    
]
