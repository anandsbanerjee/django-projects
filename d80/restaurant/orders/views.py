from datetime import date

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order, RecentOrder, OrderSpl, OrderInvoice
from .serializers import OrdersSerializer, OrderInvoiceSerializer, OrderWithInvoiceSerializer

"""
    About ViewSet, @api_view and APIView class - https://chatgpt.com/g/g-p-68e454e31e508191b259e2ae989f3da8-future-mind-consultant-product-ideas/c/69a6be2a-aac4-8398-b7ec-3cbec207734c
    Create your views here. Example of ViewSet - full CRUD in one method? all HTTP methods are covered
"""
# ------------------------------------- Start DRF View Set ----------------------------------------------------------
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrdersSerializer

class OrderInvoiceViewSet(viewsets.ModelViewSet):
    queryset = OrderInvoice.objects.all()
    serializer_class = OrderInvoiceSerializer

# Joined Data on OrderWithInvoiceSeriliazer --- >
#   Since this only from VIEW only, it inherits from viewsets.ReadOnlyModelViewSet

class OrderWithInvoiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Order.objects.select_related("invoice").all()    # OrderInvoice model as related_name = 'invoice'
    serializer_class = OrderWithInvoiceSerializer

# ------------------------------------- End DRF View Set ----------------------------------------------------------

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

#/orders/orderlist/<order_id>
@api_view(['GET'])
def get_order_by_id(request, order_id):
    order = Order.objects.get(id=order_id)
    serilizer = OrdersSerializer(order)
    return Response(serilizer.data)

# Use of Custom Query Set - OrderQuerySet
@api_view(['GET'])
def get_incomplete_orders(request):
    orders = Order.objects.in_complete()
    serializer = OrdersSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_recent_orders(request):
    recent_orders = RecentOrder.objects.all()
    serializer = OrdersSerializer(recent_orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_spl_orders(request):
    spl_orders = OrderSpl.objects.ranked_orders_raw()
    serializer = OrdersSerializer(spl_orders, many=True)
    return Response(serializer.data)





# APIView class
"""
The class-based version of @api_view. Gives you more structure — separate get(), 
post(), put() methods instead of one function with if/else. Good when you need custom logic 
that doesn't map cleanly to CRUD, or when you want to override things like authentication 
or permissions at the view level.
"""
class OrderView(APIView):
    # GET /orders/orders - summary /
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrdersSerializer(orders, many=True)
        return Response({
            "total_orders":Order.objects.all().count(),
            "pending_orders":Order.objects.filter(status='pending').count(),
            "Delivered Today":Order.objects.filter(status='Delivered', updated_at__date=date.today()).count()
        })
    #create order using APIView class -POST /orders/orders-summary/
    def post(self, request):
        serializer = OrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    # similarly def post(self, reqyest)

# /orders/orderslist/
class OrderListView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serlizer = OrdersSerializer(orders, many=True)
        return Response(serlizer.data)

# /orders/orderslist/<int:order_id>
class OrderDetailView(APIView):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        serializer = OrdersSerializer(order)
        return Response(serializer.data)