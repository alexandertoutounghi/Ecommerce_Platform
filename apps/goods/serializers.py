from rest_framework import serializers
from .models import Goods, GoodsCategory


# https://www.django-rest-framework.org/api-guide/serializers/
class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Goods
        # Can be customized to =('name', 'market_price', 'add_time')
        fields = "__all__"

    def create(self, validated_data):
        return Goods.objects.create(**validated_data)
