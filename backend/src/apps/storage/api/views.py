from rest_framework import viewsets
from apps.storage.models import Storage
from .serializers import StorageSerializer

class StorageAPIViewSet(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
