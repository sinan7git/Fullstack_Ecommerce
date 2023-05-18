from rest_framework.serializers import ModelSerializer
from ecommers.models import Products
from rest_framework import serializers


class ProductSerializer(ModelSerializer):
    
    category = serializers.SerializerMethodField()
    
    class Meta:
        fields = ("id","images","name","category",)
        model = Products
        
    def get_category(self, instance):
        return instance.category.name
        
        
class ProductDetailSerializer(ModelSerializer):
    
    category = serializers.SerializerMethodField()
    
    class Meta:
        fields = ("id","images","name","category","description")
        model = Products
        
    def get_category(self, instance):
        return instance.category.name
    
    
class CartSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = ("id","images","name","category","description")