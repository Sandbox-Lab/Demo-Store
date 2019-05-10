from rest_framework import viewsets
from apps.product.models import Product, Model
from .serializers import ProductSerializer, ModelSerializer

class ProductAPIViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ModelAPIViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer
