from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path To the differents apps.
    path('', include('bots.urls')),
    #path('adminboard/', include('admin.urls')),
    #path('', include('django.contrib.auth.urls')),
    # path admin from django.contrib admin auth.
    path('admin/', admin.site.urls),
]
