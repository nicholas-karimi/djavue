from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class LatestProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4 ]
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self, catagory_slug, product_slug):
        try:
            return Product.objects.filter(catagory_slug=catagory_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

        def get(self, request, category_slug, product_slug, format=None):
            product = self.get_object(category_slug, product_slug)
            serializer = ProductSerializer(product)

            return Response(serializer.data)