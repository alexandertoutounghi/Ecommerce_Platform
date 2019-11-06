from django.db import models

# Create your models here.
from django.utils.datetime_safe import datetime

from DjangoUeditor.models import UEditorField


class GoodsCategory(models.Model):
    """
    Goods categories
    """
    CATEGORY_TYPE = (
        (1, "First Class"),
        (2, "Second Class"),
        (3, "Third Class"),
    )

    name = models.CharField(default="", max_length=30, verbose_name="Category name", help_text="category name")
    code = models.CharField(default="", max_length=30, verbose_name="Category code", help_text="Category code")
    desc = models.TextField(default="", verbose_name="Category description", help_text="Category description")
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="Category class",
                                        help_text="Category class")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="parent category",
                                        help_text="parent category",
                                        related_name="sub_cat")
    is_tab = models.BooleanField(default=False, verbose_name="On navi-bar", help_text="is on navi bar")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add time")

    class Meta:
        verbose_name = "product category"
        verbose_name_plural = "product categories"

    def __str__(self):
        return self.name


class GoodsCategoryBrand(models.Model):
    """
    Brand name
    """
    category = models.ForeignKey(GoodsCategory, related_name='brands', null=True, blank=True,
                                 verbose_name="Goods Category")
    name = models.CharField(default="", max_length=30, verbose_name="Brand name", help_text="Brand name")
    desc = models.TextField(default="", max_length=200, verbose_name="Brand desc", help_text="Brand description")
    image = models.ImageField(max_length=200, upload_to="brands/")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add time")

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = verbose_name
        db_table = "goods_goodsbrand"

    def __str__(self):
        return self.name


class Goods(models.Model):
    """
    Goods Model
    """
    category = models.ForeignKey(GoodsCategory, verbose_name="Goods Category")
    goods_sn = models.CharField(max_length=50, default="", verbose_name="SKU")
    name = models.CharField(max_length=100, verbose_name="Goods Name")
    click_num = models.IntegerField(default=0, verbose_name="Clicks")
    sold_num = models.IntegerField(default=0, verbose_name="Sales")
    fav_num = models.IntegerField(default=0, verbose_name="favorite",
                                  help_text="How many times the product is put in wish list")
    goods_num = models.IntegerField(default=0, verbose_name="stock")
    market_price = models.FloatField(default=0, verbose_name="market price", help_text="Price in market")
    shop_price = models.FloatField(default=0, verbose_name="shop price")
    goods_brief = models.TextField(max_length=500, verbose_name="brief description")
    goods_desc = UEditorField(verbose_name="description", imagePath="goods/images/", width=1000, height=300,
                              filePath="goods/files/", default='')
    ship_free = models.BooleanField(default=True, verbose_name="is free ship", help_text="True for Free shipping")
    goods_front_image = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="front page")
    is_new = models.BooleanField(default=False, verbose_name="is new arrival")
    is_hot = models.BooleanField(default=False, verbose_name="is hot sales")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add time")

    class Meta:
        verbose_name = 'goods'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsImage(models.Model):
    """
    Goods Images
    """
    goods = models.ForeignKey(Goods, verbose_name="Goods", related_name="images")
    image = models.ImageField(upload_to="", verbose_name="Images", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add time")

    class Meta:
        verbose_name = 'Goods Images'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    """
    featured goods (banner on homepage)
    """
    goods = models.ForeignKey(Goods, verbose_name="goods")
    image = models.ImageField(upload_to='banner', verbose_name="banner images")
    index = models.IntegerField(default=0, verbose_name="sequence")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add time")

    class Meta:
        verbose_name = 'banner goods'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class HotSearchWords(models.Model):
    """
    Popular search
    """
    keywords = models.CharField(default="", max_length=20, verbose_name="Popular Search")
    index = models.IntegerField(default=0, verbose_name="Sorting")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="Added Time")

    class Meta:
        verbose_name = 'Popular Search'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.keywords


class IndexAd(models.Model):
    category = models.ForeignKey(GoodsCategory, related_name='category', verbose_name="Product Categories")
    goods = models.ForeignKey(Goods, related_name='goods')

    class Meta:
        verbose_name = 'Product Categories Advertising on HomePage'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name
