from django.contrib import admin
from django.urls import path , include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Tax_free API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.taxfree.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    validators=['ssv', 'flex'],
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/tax/', include('taxfree.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
    path('redo/c', schema_view.with_ui('redoc', cache_timeout=None), name='schema-redoc'),
]