from django.db import models
from apps.storage.models import Storage

class Model(models.Model):
    sku = models.CharField('SKU', max_length=50, blank=False, null=False, primary_key=True)

    def __str__(self):
        return self.sku

class Product(models.Model):
    imei    = models.CharField('IMEI', max_length=50, blank=False, null=False, primary_key=True)
    model   = models.ForeignKey(Model, on_delete=models.CASCADE)
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)

    def __str__(self):
        return self.imei
