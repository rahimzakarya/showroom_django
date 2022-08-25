from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.landing, name='home'),
    path('', views.landing, name='home'),
    path('products/', views.products, name='products'),
    path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    # path('products/<str:type>/<str:prod>', views.detailed_product, name='detailed_product'),
    path('products/<str:type_prod>', views.types_product, name='types_product'),
]