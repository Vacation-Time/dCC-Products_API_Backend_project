from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product


@api_view(['GET'])
def products_list(request):

    products = Product.objects.all()

    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)
