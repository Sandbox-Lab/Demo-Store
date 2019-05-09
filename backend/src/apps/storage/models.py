from django.db import models

class Storage(models.Model):
    sub  = models.CharField(max_length=50, blank=False, null=False, primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name
