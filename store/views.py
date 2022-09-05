from django.shortcuts import render
from .models import *
# Create your views here.

# 001
def landing(request):
    products_type = product_type.objects.all()
    context = {'products_type':products_type}
    return render(request, 'store/001_landing.html', context)

# 002
def types_product(request,type_prod):   
    type_prod = product_type.objects.get(name=type_prod)
    prods = products.objects.filter(type_product=type_prod)
    context = {'prods':prods, 'type_prod':type_prod}
    return render(request, 'store/002_types_product.html', context)

# 003
def products_page(request):
    product = products.objects.all()
    context = {'products':product}
    return render(request, 'store/003_products.html', context)

# 004
def view_product(request,type,prod):
    product = products.objects.get(name=prod)
    product_options = options_product.objects.filter(product=product)

    context = {'product':product, 'product_options':product_options}
    return render(request, 'store/005_view_product.html', context)

# 005
def contact(request):
    context = {}
    return render(request, 'store/006_contact.html', context)

# 000
def handle_not_found(request, exception):
    context = {}
    return render(request, 'store/000_not-found.html', context)

