
from django.urls import path, include

from django.contrib import admin
from expos import views



urlpatterns = [
    path(r'', views.index, name="index"),
    path(r'', include('expos.urls')),
    path(r'admin/', admin.site.urls),
]


