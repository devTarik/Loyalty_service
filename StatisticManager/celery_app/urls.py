from django.contrib import admin
from django.urls import path,include
from celery_app.views import *
from celery_app.services import balance

urlpatterns = [
    path('new_operation/', check_new_operation),
]
