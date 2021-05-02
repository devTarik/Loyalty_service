from django.urls import path, include
from points_app.views import *

urlpatterns = [
   path('client/create/', NewClient.as_view()),
   path('client/list/', ClientList.as_view()),
   path('client/detail/<int:pk>/', ClientDetail.as_view()),
   path('operations/list/', OperationsList.as_view()),
   path('operations/create/', NewOperation.as_view()),
   path('operations/detail/<int:pk>/', OperationDetail.as_view()),
   
   # for Celery 
   path('nopermition/all/', NopermitionClientAll.as_view()),
   path('nopermition/detail/<int:pk>/', NopermitionClientDetail.as_view()),
]