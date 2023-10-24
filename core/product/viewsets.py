from core.abstract.viewsets import AbstractViewSet
from core.product.models import Product
from core.product.serializers import ProductSerializer
from rest_framework import filters

from django.http.response import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.core.cache import cache
import uuid


class ProductViewSet(AbstractViewSet):
    http_method_names = ("get", "put")
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # All data will be sent to front-end, and will be paginated at there.
    pagination_class = None

    def get_queryset(self):
        title = self.request.query_params.get('title')
        if title:
            self.queryset = Product.objects.filter(title__icontains=title)
        return self.queryset

    def put(self, request, *args, **kwargs):
        id = self.request.query_params.get('id')
        try:
            product = Product.objects.get(public_id=uuid.UUID(id))
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
