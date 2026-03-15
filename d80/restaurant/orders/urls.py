from django.urls import include, path
from rest_framework import routers

from .views import OrderViewSet, orders, OrderView

#create a router
router = routers.DefaultRouter()
router.register('', OrderViewSet, basename='orders')

urlpatterns = [
    #Router based url path for APIViewSet type views
    path('items/', include(router.urls)),

    #function decorator based paths - @api_view
    path('orderlist/', orders, name='orders'),

    #APIView class based views
    path('orders-summary/', OrderView.as_view(), name='orders-summary'),
]