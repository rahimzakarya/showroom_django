from django.db import models

# Create your models here.

class product_type(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=800, null=True)

    def __str__(self):
        return self.name



class product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    type_product = models.ForeignKey(product_type, on_delete=models.CASCADE, null=True)

    price = models.FloatField()
    price_unit = models.CharField(default='da / pieces',  max_length=20)
    description = models.CharField(max_length=800, null=True, blank=True)

    def __str__(self):
        return self.name