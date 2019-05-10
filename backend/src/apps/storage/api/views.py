from rest_framework import generics
from apps.storage.models import Storage
from .serializers import StorageSerializer

class StorageListAPIView(generics.ListAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer

class StorageRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
