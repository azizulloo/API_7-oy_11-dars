from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,IsAuthenticatedOrReadOnly
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.pagination import PageNumberPagination


from .models import Car
from .serializers import CarSerializer
from .permissions import MyPermission


# Pagination Class
class CarPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'  
    max_page_size = 100


class CartApiView(generics.ListCreateAPIView):
    queryset=Car.objects.order_by('-id')
    serializer_class=CarSerializer
    permission_classes = [MyPermission]
    pagination_class = CarPagination

    filter_backends=[DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['price', 'year', 'max_speed']
    search_fields = ['car_name', 'engine', 'brand__name']
    ordering_fields=['id', 'car_name', 'year', 'max_speed', 'price']
    throttle_scope = 'cars'





    
    def get_queryset(self):
        q=self.queryset.all()
        return q
    
    def get_serializer_class(self):
        return super().get_serializer_class()
    
    
    
class CarDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Car.objects.all()
    serializer_class=CarSerializer
    lookup_url_kwarg='car_id'
    lookup_field='pk'
    permission_classes=[permissions.DjangoModelPermissions]
    
    
    
    