from django.db import models

class Storage(models.Model):
    sub_inv = models.CharField('Sub Inventory', max_length=50, blank=False, null=False, primary_key=True)
    pdv     = models.CharField('Name', max_length=100, blank=False, null=False)

    def __str__(self):
        return self.pdv
