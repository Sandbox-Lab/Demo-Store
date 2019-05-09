from django.db import models
from .storage.models import Storage

class Product(models.Models):
    sku     = models.CharField(max_length=50, blank=False, null=False, primary_key=True)
    imei    = models.CharField(max_length=50, blank=False, null=False, unique=True)
    storage = ForeignKey(Storage, on_delete=models.CASCADE)
