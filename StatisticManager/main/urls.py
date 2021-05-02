from django.urls import path,include

urlpatterns = [
    path('', include('celery_app.urls'))
]
