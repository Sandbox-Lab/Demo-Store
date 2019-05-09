from django.db import models
from apps.storage.models import Storage

class Product(models.Model):
    sku     = models.CharField(max_length=50, blank=False, null=False, primary_key=True)
    imei    = models.CharField(max_length=50, blank=False, null=False, unique=True)
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)