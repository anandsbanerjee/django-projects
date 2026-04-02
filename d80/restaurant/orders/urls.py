from django.urls import include, path
from rest_framework import routers

from .views import OrderViewSet, orders, OrderView, get_order_by_id, OrderListView, OrderDetailView, get_recent_orders, \
    get_spl_orders, OrderInvoiceViewSet, OrderWithInvoiceViewSet, get_incomplete_orders

#create a router
router = routers.DefaultRouter()

#register router for each ViewSet in the project
router.register('items', OrderViewSet, basename='items')
router.register('invoices', OrderInvoiceViewSet, basename='invoices')
router.register('orderinvoices', OrderWithInvoiceViewSet, basename='orderinvoices')

urlpatterns = [
    #Router based url path for APIViewSet type views
    path('', include(router.urls)),

    #function decorator based paths - @api_view
    path('orderlist/', orders, name='orders'),
    path('orderlist/<int:order_id>', get_order_by_id, name='get_order_by_id'),
    path('orderlist/recent/', get_recent_orders, name='recent-orders'),
    path('orderlist/specials', get_spl_orders, name='special-orders'),
    path('orderlist/incomplete', get_incomplete_orders, name='incomplete-orders'),

    #APIView class based views
    path('orders-summary/', OrderView.as_view(), name='orders-summary'),
    path('orderslist/', OrderListView.as_view(), name='orders-lists-view'),
    path('orderslist/<int:order_id>', OrderDetailView.as_view(), name='orders-details-view'),
]