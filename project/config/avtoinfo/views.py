from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.throttling import ScopedRateThrottle

from .models import Car, Brand, Color
from .serializers import CarSerializer, BrandSerializer, ColorSerializer
from .permissions import MyPermission



# Pagination Class
class MyPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100



#Cars
class CarApiView(generics.ListCreateAPIView):
    queryset = Car.objects.select_related('brand', 'color').order_by('-id')
    serializer_class = CarSerializer
    pagination_class = MyPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['price', 'year', 'max_speed', 'brand', 'color']
    search_fields = ['car_name', 'engine', 'brand__name']
    ordering_fields = ['id', 'car_name', 'year', 'max_speed', 'price']
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'cars'

    def get_permissions(self):
        """Read uchun — ruxsat hammaga, yozish uchun — faqat admin"""
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [MyPermission(), permissions.IsAdminUser()]



class CarDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'car_id'
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'cars'

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [MyPermission(), permissions.IsAdminUser()]




#Brands
class BrandCreateView(generics.ListCreateAPIView):
    queryset = Brand.objects.order_by('-id')
    serializer_class = BrandSerializer
    pagination_class = MyPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'brands'

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [MyPermission(), permissions.IsAdminUser()]




class BrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'brand_id'
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'brands'

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [MyPermission(), permissions.IsAdminUser()]




#Colors
class ColorCreateView(generics.ListCreateAPIView):
    queryset = Color.objects.order_by('-id')
    serializer_class = ColorSerializer
    pagination_class = MyPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'hex']
    ordering_fields = ['id', 'name']
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'colors'

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [MyPermission(), permissions.IsAdminUser()]



class ColorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'color_id'
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'colors'

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [MyPermission(), permissions.IsAdminUser()]
