# Create your views here.
from rest_framework.response import Response


from .models import Goods, GoodsCategory
from .serializers import GoodsSerializer, CategorySerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend
from .filters import GoodsFilter


# from rest_framework_extensions.cache.mixins import CacheResponseMixin



# https://www.django-rest-framework.org/api-guide/generic-views/
# If front end needs 30 items per page: goods/?p=2&page_size=30
class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    Product List, Pagination, Search, Filter, Ordering

    """
    # throttle_classes = (UserRateThrottle, )
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    # authentication_classes = (TokenAuthentication, )
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'shop_price')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CategoryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        List all categories
    retrieve:
        List category detail
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer


class HotSearchsViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Get popular search list
    """
    queryset = HotSearchWords.objects.all().order_by("-index")
    serializer_class = HotWordsSerializer


class BannerViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Get featured product list, banners on home page
    """
    queryset = Banner.objects.all().order_by("index")
    serializer_class = BannerSerializer


class IndexCategoryViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Product categories data on home page
    """
    queryset = GoodsCategory.objects.filter(is_tab=True, name__in=["FreshFood", "Drinks"])
    serializer_class = IndexCategorySerializer
