"""
URL configuration for projects project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import prodcut_detail_view, greet, health_check, WelcomeView, GreetView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/<str:sku>/', prodcut_detail_view, name='product-detail'),
    path('greet/', greet),
    path('greet/<str:username>/', GreetView.as_view(), name='greet'),
    path('health/', health_check, name='health'),
    path('welcome/<str:name>/', WelcomeView, name='welcome'),
]