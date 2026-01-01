from django.shortcuts import render
from .models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
# Create your views here.

class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        ser_data = ProductSerializer(products, many=True)
        return Response(ser_data.data)