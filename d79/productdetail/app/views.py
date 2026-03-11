from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.views import View

# Create your views here.

# dummy data
products = [
                  {
                    "sku": "SKU123",
                    "name": "Laptop",
                    "price": 999.99,
                    "currency": "USD"
                  },
                  {
                    "sku": "SKU456",
                    "name": "Mechanical Keyboard",
                    "price": 89.50,
                    "currency": "USD"
                  },
                  {
                    "sku": "SKU789",
                    "name": "Mechanical Keyboard",
                    "price": 120.00,
                    "currency": "USD"
                  },
                  {
                    "sku": "SKU023",
                    "name": "27-inch Monitor",
                    "price": 299.99,
                    "currency": "USD"
                  },
                  {
                    "sku": "SKU145",
                    "name": "USB-C Docking Station",
                    "price": 85.75,
                    "currency": "USD"
                  }
            ]

# function based view - Q1
def prodcut_detail_view(request, sku):
    # Allow only GET requests
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])

    # convert the input sku from int to string
    sku = (str(sku))

    # iterate through the products disctionary to find the sku match
    for product in products:
        if product["sku"] == sku:
            return JsonResponse(product, status=200)
    #if product not found, return error message
    return JsonResponse({"error": "product not found"}, status=404)

    # return HttpResponse('Product Detail View - {}'.format(sku))

def get_products(request):
    context = {
        'products': products
    }
    return JsonResponse(context)
# Q3 - MCQ - /greet and /greet/{name} with default value
def greet(request, name="Guest"):
    return HttpResponse(f"Hello, {name}!")


#Q3 - Create a simple health-check endpoint using a function-based view in Django.
def health_check(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    return HttpResponse("OK", content_type="text/plain", status=200)

# Q4. Welcome Endpoint
def WelcomeView(request, name):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    return HttpResponse(f" Welcome to Django, {name}!", content_type="text/plain", status=200)

# Q2. Greeting with path + query params - class based views
class GreetView(View):
    def get(self, request, username):
        http_method_names = ['get']
        lan = request.GET.get('lang', 'en')
        if lan == 'hi':
            greeting = 'Namaste, {}!'.format(username)
        else:
            greeting = 'Hello, {}!'.format(username)

        return HttpResponse(greeting, content_type="text/plain", status=200)

