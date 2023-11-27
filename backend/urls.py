from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions, routers
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from backend.api import views

schema_view = get_schema_view(
   openapi.Info(
      title="Task API",
      default_version='v1',
      description="API for Task model. Provides full CRUD functinality.",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('tasks', views.TaskViewSet, basename='Task')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/sign-in', obtain_auth_token),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include(router.urls)),
]
