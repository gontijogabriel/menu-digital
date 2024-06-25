from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from product.serializers import ProductSerializer
from product.models import Product

class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
