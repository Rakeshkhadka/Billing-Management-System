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
        History.objects.get_or_create(remarks=f"{instance.name} by {request.user}")
        self.perform_destroy(instance)
        return Response({"message": "bhayo hai guys"}, status=status.HTTP_204_NO_CONTENT)
    
    def list(self, request, *args, **kwargs):
        res = super().list(request, *args, **kwargs)
        q_count = self.queryset.count()
        v_count = self.queryset.filter(status='verified').count()
        un_count = q_count - v_count
        # client_status = {
        #     'total_client': q_count,
        #     'total_verified':v_count,
        #     'total_unverified': un_count
        # }
        # mycount = dict(q_count=q_count)
        # res.data.extend([client_status])
        res.data.extend([{
            'total_client': q_count,
            'total_verified':v_count,
            'total_unverified': un_count
        }])
        # queryset = self.filter_queryset(self.get_queryset())
        # queryset_count = queryset.count()
        # mycount = dict(q_count=queryset_count)
        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)
        # serializer = self.get_serializer(queryset, many=True)
        # result = serializer.data, mycount
        # return Response(serializer.data)
        return Response(res.data )
    
    
# from django.http import HttpResponse
# from .models import *
# from faker import Faker
# fake = Faker()

# def feed_data(request):
#     for _ in range(10):
#         client_data = {
#             'name': fake.name(),
#             'email': fake.email(),
#             'organization_size' : fake.random_element(ORGANIZATION_SIZE_CHOICES)[0],
#             'expiry_date': fake.date(),
#             'country': fake.country(),
#             'status' : fake.random_element(STATUS_CHOICES)[0]
#         }
#         domain = client_data['name'].split(' ')[0] + 'realhrsoft.com.np'
#         Client.objects.create(domain = domain, **client_data)
#     return HttpResponse("fake data feeded") 