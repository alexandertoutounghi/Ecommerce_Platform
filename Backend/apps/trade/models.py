from django.db import models
# First approach to import a model
from django.contrib.auth import get_user_model
# Another approach to import a model
from django.utils.datetime_safe import datetime

from goods.models import Goods

# Create your models here.
User = get_user_model()


class ShoppingCart(models.Model):
    """
    Shopping cart model design
    """
    user = models.ForeignKey(User, verbose_name="User")
    goods = models.ForeignKey(Goods, verbose_name="Goods")
    nums = models.IntegerField(default=0, verbose_name="Purchase Quantity")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="Add time")

    class Meta:
        verbose_name = 'Shopping Cart'
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")

    def __str__(self):
        return "%s(%d)".format(self.goods.name, self.nums)


class OrderInfo(models.Model):
    """
    Orders

    """
    ORDER_STATUS = (
        ("TRADE_SUCCESS", "Success"),
        ("TRADE_CLOSED", "Timeout"),
        ("WAIT_BUYER_PAY", "Transaction Created"),
        ("TRADE_FINISHED", "Transaction Completed"),
        ("PAYING", "Waiting For Payment"),
    )
    PAY_TYPE = (
        ("PAYPAL", "PayPal"),
        ("CREDIT_CARD", "Credit Card")
    )

    user = models.ForeignKey(User, verbose_name="User")
    order_sn = models.CharField(max_length=30, null=True, blank=True, unique=True, verbose_name="Order Number")
    trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name="Transaction Number")
    pay_status = models.CharField(choices=ORDER_STATUS, default="PAYING", max_length=30, verbose_name="Payment Status")
    pay_method = models.CharField(choices=PAY_TYPE, default="PAYPAL", max_length=30, verbose_name="Payment Method")
    post_script = models.CharField(max_length=200, verbose_name="Order Comment")
    order_mount = models.FloatField(default=0.0, verbose_name="Order Amount")
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name="Pay Time")

    # User Info

    address = models.CharField(max_length=100, default="", verbose_name="Shipping Address")
    signer_name = models.CharField(max_length=20, default="", verbose_name="Receipt")
    singer_mobile = models.CharField(max_length=11, verbose_name="Phone Number")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="add time")

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)


class OrderGoods(models.Model):
    """
    Detailed description for ordered product
    """
    order = models.ForeignKey(OrderInfo, verbose_name="Order Detail", related_name="goods")
    goods = models.ForeignKey(Goods, verbose_name="Goods")
    goods_num = models.IntegerField(default=0, verbose_name="Goods Quantity")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add time")

    class Meta:
        verbose_name = "Order Detail"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_sn)
