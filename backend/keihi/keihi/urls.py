from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Keihi Kanri API",
        default_version='v1',
        description="API de um gerenciador de pagamentos e gastos",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="emanuelvilela.dev@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('payment.urls')),
    path('api/', include('daywork.urls')),
    path('api/', include('work.urls')),
    path('api/', include('health.urls')),
    path('api/', include('resources.urls')),
]
