
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from expos import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
#router.register(r'sample', views.SampleViewSet)
router.register(r'expo', views.ExpoViewSet)
router.register(r'obra', views.ObraViewSet)
router.register(r'comentario', views.ComentarioViewSet)
#router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.

urlpatterns = [
    path(r'api/', include(router.urls)),
    path(r'api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
