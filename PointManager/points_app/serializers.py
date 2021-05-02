from rest_framework import serializers
from points_app.models import Client, Operations


class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ClientListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class OperationsSerializers (serializers.ModelSerializer):
    class Meta:
        model = Operations
        fields = ('client', 'descript', 'act', 'points')
        
class OperationsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Operations
        fields = ('client', 'descript', 'act', 'points','date')

        