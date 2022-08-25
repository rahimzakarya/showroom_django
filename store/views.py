from django.shortcuts import render
from .models import *
# Create your views here.

def about(request):

    context = {}
    return render(request, 'store/about.html', context)

# def contact(request):
#     context = {}
#     return render(request, 'store/contact.html', context)

def products(request):
    products = product.objects.all()
    context = {'products':products}
    return render(request, 'store/products.html', context)

def landing(request):
    products = product.objects.all()
    products_type = product_type.objects.all()
    context = {'products_type':products_type, 'products':products}
    return render(request, 'store/landing.html', context)

# def detailed_product(request,type,prod):
#     data = product.objects.get(name=prod)
#     product_sim = product_type.objects.all()
#     context = {'product':data, 'product_sim': product_sim}
#     return render(request, 'store/detailed_product.html', context)

def types_product(request,type_prod):
    data = product.objects.all()
    data_type = product_type.objects.filter(name=type_prod)
    context = {'data':data, 'data_type':data_type}
    return render(request, 'store/types_product.html', context)