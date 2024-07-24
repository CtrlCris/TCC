from rest_framework import serializers
from myapp.models import Category,Products,SubProducts
import django_filters

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Products
    fields = '__all__'

class SubProductsSerializer(serializers.ModelSerializer):
  class Meta:
    model = SubProducts
    fields = '__all__'