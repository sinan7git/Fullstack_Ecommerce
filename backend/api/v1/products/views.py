from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from ecommers.models import Products
from api.v1.products.serializers import ProductSerializer,ProductDetailSerializer,CartSerializer

@api_view(["GET"])
def products(request):
    instances = Products.objects.filter(is_deleted=True)
    
    q = request.GET.get("q")
    if q:
        ids = q.split(",")
        instances = instances.filter(category__in=ids)
    
    context = {
        "request": request
    }
    serializer = ProductSerializer(instances, many=True, context=context)
    response_data = {
        "status_code": 6000,
        "data": serializer.data
    }
    
    return Response(response_data)


@api_view(["GET"])
def product(request,pk):
    if Products.objects.filter(pk=pk).exists():
        instance = Products.objects.get(pk=pk)
        
        context = {
            "request":request
        }
        serializer = ProductDetailSerializer(instance,context=context)
        
        response_data = {
            "status_code" : 6000,
            "data" : serializer.data
        }
        return Response(response_data)
    else:
        response_data = {
            "status_code" : 6000,
            "message" : "Product Not Exist"
        }
        
        return Response(response_data)
    
    
@api_view(["GET"])
def add_cart(request):
    instances = Products.objects.filter(add_cart=True)
    context = {
        "request":request
    }
    serializer = CartSerializer(instances, many=True, context=context)
    
    response_data = {
        "status_code": 6000,
        "data": serializer.data
    }
    return Response(response_data)


@api_view(['POST'])
def add_to_cart(request,pk):
    instance = get_object_or_404(Products, pk=pk)
    serializer = CartSerializer(instance, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save(add_cart=True)
        return Response({"status_code": 600, "message": "Added to Cart"})
    return Response({"status_code": 601, "message": "Validation error", "data": serializer.errors})



@api_view(['DELETE'])
def delete_cart_item(request, pk):
    cart_item = get_object_or_404(Products, pk=pk)
    cart_item.add_cart = False  
    cart_item.save()
    return Response({"status_code": 200, "message": "Item removed from cart"})