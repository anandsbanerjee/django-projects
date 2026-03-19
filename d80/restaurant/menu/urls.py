from django.urls import path, include

from menu import views
from .views import MenuItemsViewSet, CategoryViewSet, MenuItemsWithCategoryViewSet, MenuItemsWithCategoryFlattenViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('menu-items', views.MenuItemsViewSet, basename='menu-items')
router.register('categories', views.CategoryViewSet, basename='categories')
router.register('menu-details', views.MenuItemsWithCategoryViewSet, basename='menu-details')
router.register('menu-flattend', views.MenuItemsWithCategoryFlattenViewSet, basename='menu-flattend')


urlpatterns = [
    #Router based url path for APIViewSet type views
    path('', include(router.urls)),

    path('', views.home, name='home'),
    path('items', views.menu, name='menuitems'),
    path('items/<int:id>', views.menu_item, name='item-detail'),
]