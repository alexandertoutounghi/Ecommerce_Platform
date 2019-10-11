# Create your views here.
from .models import Goods
from .serializers import GoodsSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination


# https://www.django-rest-framework.org/api-guide/generic-views/
# If front end needs 30 items per page: goods/?p=2&page_size=30
class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "p"
    max_page_size = 100


class GoodsListView(generics.ListAPIView):
    """
    List all goods
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
