from django.shortcuts import render
from django.http import HttpResponse
from .models import History, Client
from .serializers import ClientSerializer
from rest_framework.response import Response
# Create your views here.

from rest_framework import viewsets, status


class ClientViewset(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print(request.user)
        History.objects.get_or_create(remarks=instance.name)
        # self.perform_destroy(instance)
        super().destroy(instance)
        return Response({"message": "bhayo hai guys"}, status=status.HTTP_204_NO_CONTENT)
    
    def get_queryset(self):
        return Client.objects.all()