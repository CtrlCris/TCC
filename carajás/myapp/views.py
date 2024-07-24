from django.shortcuts import render
from rest_framework import generics, viewsets, permissions, filters
from .models import Category, Products, SubProducts
from carajás.serializers import CategorySerializer, ProductsSerializer, SubProductsSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class CategoryList(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

class ProductsList(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = [
        "get",
        "post",
        "put",
        "delete",
    ]
    filterset_fields = [
        "category_id",
    ]
    

class SubProductsList(viewsets.ModelViewSet):
    queryset = SubProducts.objects.all()
    serializer_class = SubProductsSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    http_method_names = [
        "get",
        "post",
        "put",
        "delete",
    ]
    filterset_fields = [
        "product_id",
    ]
