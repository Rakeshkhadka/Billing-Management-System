from django.shortcuts import render
from django.http import HttpResponse
from .models import History, Client
from .serializers import ClientSerializer
from rest_framework.response import Response
# Create your views here.

from rest_framework import viewsets, status
from rest_framework.decorators import action

from django.shortcuts import get_object_or_404


# class ClientViewset(viewsets.ModelViewSet):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         print(request.user)
#         History.objects.get_or_create(remarks=f"{instance.name} by {request.user}")
#         self.perform_destroy(instance)
#         return Response({"message": "bhayo hai guys"}, status=status.HTTP_204_NO_CONTENT)
    
#     def list(self, request, *args, **kwargs):
#         res = super().list(request, *args, **kwargs)
#         q_count = self.queryset.count()
#         v_count = self.queryset.filter(status='verified').count()
#         un_count = q_count - v_count
#         res.data.extend([{
#             'total_client': q_count,
#             'total_verified':v_count,
#             'total_unverified': un_count
#         }])
    
#         return Response(res.data )
    
#     @action(detail=False, methods=['GET'], url_path='verifiedclient')
#     def verified(self, request, *args, **kwargs):
#         verified_client = self.queryset.filter(status='verified')
#         serializer = self.get_serializer(verified_client, many=True)
#         return Response(serializer.data)
#     @action(detail=False, methods=['GET'])
#     def unverified(self, request, *args, **kwargs):
#         verified_client = Client.objects.filter(status='unverified')
#         serializer = ClientSerializer(verified_client, many=True)
#         return Response(serializer.data)


class ClientViewset(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print(request.user)
        History.objects.get_or_create(remarks=f"{instance.name} by {request.user}")
        self.perform_destroy(instance)
        return Response({"message": "bhayo hai guys"}, status=status.HTTP_204_NO_CONTENT)
    
    def list(self, request, *args, **kwargs):
        res = super().list(request, *args, **kwargs)
        q_count = self.queryset.count()
        v_count = self.queryset.filter(status='verified').count()
        un_count = q_count - v_count
        res.data.extend([{
            'total_client': q_count,
            'total_verified':v_count,
            'total_unverified': un_count
        }])
    
        return Response(res.data )
    
    @action(detail=False, methods=['GET'])
    def verified(self, request, *args, **kwargs):
        verified_client = self.queryset.filter(status='verified')
        serializer = self.get_serializer(verified_client, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['GET'])
    def unverified(self, request, *args, **kwargs):
        verified_client = Client.objects.filter(status='unverified')
        serializer = ClientSerializer(verified_client, many=True)
        return Response(serializer.data)

    
