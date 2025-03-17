from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from .filtters import ProductFilter
@api_view(['GET'])
def get_all_product(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_product_filtered(request):
    filterset = ProductFilter(request.GET,queryset=Product.objects.all().order_by('id'))
    serializer = ProductSerializer(filterset.qs,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_one_product(request,pk):
    product = get_object_or_404(Product,id=pk)
    serializer = ProductSerializer(product,many=False).data
    return Response(serializer)
# Create your views here.
