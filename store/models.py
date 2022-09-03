from django.db import models

# Create your models here.

class product_type(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=800, null=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/products/{self.name}'


class products(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    brand = models.CharField(max_length=100, null=False, blank=False, default='')
    type_product = models.ForeignKey(product_type, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True)
    price = models.FloatField()
    price_unit = models.CharField(default='da/pieces',  max_length=20)
    description = models.CharField(max_length=800, null=True, blank=True)
    options_dispo = models.BooleanField(default=False)
    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return f'/products/{self.type_product}/{self.name}'


class options_product(models.Model):
    name = models.CharField(max_length=100, null=True, blank=False)
    product = models.ForeignKey(products, on_delete=models.CASCADE, null=True)
    price = models.FloatField()
    price_unit = models.CharField(default='da/pieces',  max_length=20)
    description = models.CharField(max_length=800, null=True, blank=True)
    def __str__(self):
        return str(self.name)