from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import MenuItem, Category

menu_items = [
    {"id": 1, "name": "Tea", "price": 10.00, "category": "Beverage"},
    {"id": 2, "name": "Coffee", "price": 15.00, "category": "Beverage"},
    {"id": 3, "name": "Masala Dosa", "price": 60.00, "category": "South Indian"},
    {"id": 4, "name": "Veg Sandwich", "price": 45.00, "category": "Snacks"},
    {"id": 5, "name": "Paneer Roll", "price": 70.00, "category": "Snacks"},
    {"id": 6, "name": "Chicken Biryani", "price": 180.00, "category": "Main Course"},
    {"id": 7, "name": "Veg Fried Rice", "price": 120.00, "category": "Main Course"},
    {"id": 8, "name": "Gulab Jamun", "price": 40.00, "category": "Dessert"},
    {"id": 9, "name": "Ice Cream", "price": 50.00, "category": "Dessert"},
    {"id": 10, "name": "Fresh Lime Soda", "price": 30.00, "category": "Beverage"}
]

menu_items = MenuItem.objects.all()

# Create your views here.
def home(request):
    return HttpResponse("Hello, world. Welcome to the restaurant menu home page.")

def menu(request):
    context = {
        'menu_items': menu_items
    }
    return render(request, 'menu/menuitems.html', context)

def menu_item(request, id):
    menu_item = MenuItem.objects.get(id=id)
    context = {
        'menu_item': menu_item
    }
    return render(request, 'menu\itemdetail.html', context)
# This method is to use hardcoded list object declared above "menu_items.
def menu_item_old(request, id):
    for item in menu_items:
        # Referencing the id in a way its done for Python List object
        if item["id"] == id:
            return JsonResponse({"menu_item": item})
    return HttpResponse("Item - {} not found".format(id))

# Apply CRUD using Django Rest Framework (DRF)