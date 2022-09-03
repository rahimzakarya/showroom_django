from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(product_type)
admin.site.register(products)
admin.site.register(options_product)