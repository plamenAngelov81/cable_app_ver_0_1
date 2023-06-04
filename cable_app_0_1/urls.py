
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cable_app_0_1.users.urls')),
    path('', include('cable_app_0_1.cable.urls')),
]
