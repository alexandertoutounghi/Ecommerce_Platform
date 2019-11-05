from django.db import models
from django.contrib.auth import get_user_model
from django.utils.datetime_safe import datetime

from goods.models import Goods

# Create your models here.
User = get_user_model()


class UserFav(models.Model):
    """
    User Favorite
    """
    user = models.ForeignKey(User, verbose_name="User")
    goods = models.ForeignKey(Goods, verbose_name="Goods", help_text="Product Id")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="Add Time",
                                    help_text="When the item is added in wish list")

    class Meta:
        verbose_name = 'User Favorite'
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")

    def __str__(self):
        return self.user.username


class UserLeavingMessage(models.Model):
    """
    User Comments
    """
    MESSAGE_CHOICES = (
        (1, "Comment"),
        (2, "Complaint"),
        (3, "Inquiry"),
        (4, "After Sales"),
        (5, "Suggestion")
    )
    user = models.ForeignKey(User, verbose_name="User")
    message_type = models.IntegerField(default=1, choices=MESSAGE_CHOICES, verbose_name="Message Type",
                                       help_text="Message Type: 1(Comment),2(Complaint),3(Inquiry),4(After Sales),"
                                                 "5(Suggestion)")
    subject = models.CharField(max_length=100, default="", verbose_name="Subject")
    message = models.TextField(default="", verbose_name="Content", help_text="Content")
    file = models.FileField(upload_to="message/images/", verbose_name="Uploaded File", help_text="Uploaded File")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="Add Time")

    class Meta:
        verbose_name = "User Comments"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject


class UserAddress(models.Model):
    user = models.ForeignKey(User, verbose_name="User")
    province = models.CharField(max_length=100, default="", verbose_name="Province")
    city = models.CharField(max_length=100, default="", verbose_name="City")
    district = models.CharField(max_length=100, default="", verbose_name="District")
    address = models.CharField(max_length=100, default="", verbose_name="Detail Address")
    signer_name = models.CharField(max_length=100, default="", verbose_name="Signer")
    signer_mobile = models.CharField(max_length=10, default="", verbose_name="Phone Number")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="Add Time")

    class Meta:
        verbose_name = "Delivery Address"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address
