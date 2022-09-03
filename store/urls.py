from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing, name='home'),       # => 001
    path('home/', views.landing, name='home'),  # => 001
    path('products/', views.products_page, name='products'), # => 002
    path('contact/', views.contact, name='contact'),    # => 003
    path('products/<str:type>/<str:prod>', views.view_product, name='view_product'),    # => 004
    path('products/<str:type_prod>', views.types_product, name='products_types'),   # => 005
]