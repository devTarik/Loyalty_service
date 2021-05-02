from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from points_app.serializers import *
from points_app.models import *
import requests


class NewClient (generics.CreateAPIView):

    serializer_class = ClientSerializers
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ClientList (generics.ListAPIView):

    serializer_class = ClientListSerializers
    
    def get_queryset(self):
        queryset = Client.objects.filter(user=self.request.user)
        return queryset


class ClientDetail (generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ClientSerializers

    def get_queryset(self):
        queryset = Client.objects.filter(user=self.request.user)
        return queryset


class NewOperation (APIView):

    def post(self, request):
        serializer = OperationsSerializers(data=request.data)
        try:
            if serializer.is_valid():
                req_client = request.data.get('client')
                req_act = bool(request.data.get('act'))
                req_point = request.data.get('points')
                get_client = Client.objects.filter(id=req_client, user=request.user).first()
                if req_act == True:
                    get_client_points = get_client.points
                    get_client.points = get_client_points + req_point
                elif req_act == False:
                    get_client_points = get_client.points
                    if req_point <=get_client_points:
                        get_client.points = get_client_points - req_point
                    else:
                        return Response('Not enough points', status=status.HTTP_406_NOT_ACCEPTABLE)
                get_client.save()
                serializer.save()
                try: # send request to Celery for run task 'control_balance'
                    requests.get(f'http://127.0.0.1:8081/new_operation/?client_id={req_client}')
                finally:
                    return Response('OK', status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OperationsList (generics.ListAPIView):

    serializer_class = OperationsListSerializers

    def get_queryset(self):
        queryset = Operations.objects.filter(client__user=self.request.user)
        return queryset


class OperationDetail (generics.RetrieveUpdateDestroyAPIView):

    serializer_class = OperationsSerializers

    def get_queryset(self):
        queryset = Operations.objects.filter(client__user=self.request.user)
        return queryset

# for Celery
class NopermitionClientAll (generics.ListAPIView):
    permission_classes = [permissions.AllowAny]

    serializer_class = ClientListSerializers
    queryset = Client.objects.all()
        
# for Celery
class NopermitionClientDetail (generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]

    serializer_class = ClientListSerializers
    queryset = Client.objects.all()
