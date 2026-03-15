from datetime import date

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .serializers import OrdersSerializer
from ...animal.app.models import Weather
from ...animal.app.serializers import WeatherSerializer


# About ViewSet, @api_view and APIView class - https://chatgpt.com/g/g-p-68e454e31e508191b259e2ae989f3da8-future-mind-consultant-product-ideas/c/69a6be2a-aac4-8398-b7ec-3cbec207734c

# Create your views here. Example of ViewSet - full CRUD in one method? all HTTP methods are covered
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrdersSerializer

# Function based decorators - used for non CRUD operations
@api_view(['GET','POST'])
def orders(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrdersSerializer(orders, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)



# APIView class
"""
The class-based version of @api_view. Gives you more structure — separate get(), 
post(), put() methods instead of one function with if/else. Good when you need custom logic 
that doesn't map cleanly to CRUD, or when you want to override things like authentication 
or permissions at the view level.
"""
class OrderView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrdersSerializer(orders, many=True)
        return Response({
            "total_orders":Order.objects.all().count(),
            "pending_orders":Order.objects.filter(status='pending').count(),
            "Delivered Today":Order.objects.filter(status='Delivered', updated_at__date=date.today()).count()
        })
    # similarly def post(self, reqyest)