from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
# Create your views here.

class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        # print(products)
        ser_data = ProductSerializer(products, many=True)
        return Response(ser_data.data , status=status.HTTP_200_OK)