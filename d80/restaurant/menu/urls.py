from django.urls import path

from menu import views

urlpatterns = [
    path('', views.home, name='home'),
    path('items', views.menu, name='menuitems'),
    path('items/<int:id>', views.menu_item, name='item-detail'),
]