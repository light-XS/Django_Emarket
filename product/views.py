from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from .filtters import ProductFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
# pagination
paginator = PageNumberPagination()
paginator.page_size = 2
#############
@api_view(['GET'])
def get_all_product(request):
    products = Product.objects.all()
    count = products.count()
    queryset = paginator.paginate_queryset(products,request)
    serializer = ProductSerializer(queryset,many=True)
    return Response({"data":serializer.data,"count":count},status=status.HTTP_200_OK)

@api_view(['GET'])
def get_product_filtered(request):
    filterset = ProductFilter(request.GET,queryset=Product.objects.all().order_by('id'))
    count = filterset.qs.count()  # count of elimen
    queryset = paginator.paginate_queryset(filterset.qs,request)
    serializer = ProductSerializer(queryset,many=True)
    return Response({"data":serializer.data,"count":count},status=status.HTTP_200_OK)

@api_view(['GET'])
def get_one_product(request,pk):
    product = get_object_or_404(Product,id=pk)
    serializer = ProductSerializer(product,many=False).data
    return Response(serializer)
# Create your views here.
