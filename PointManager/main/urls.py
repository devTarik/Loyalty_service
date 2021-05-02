from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/points/', include('points_app.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
