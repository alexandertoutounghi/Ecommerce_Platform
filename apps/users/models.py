from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.utils.datetime_safe import datetime


class UserProfile(AbstractUser):
    first_name = models.CharField(max_length=30, null=False, blank=True, verbose_name="first name")
    last_name = models.CharField(max_length=30, null=False, blank=True, verbose_name="last name")
    birthday = models.DateField(null=True, blank=True, verbose_name="birthday")
    gender = models.CharField(max_length=6, choices=(("male", u"male"), ("female", "male")), default="female",
                              verbose_name="gender")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="mobile")
    email = models.EmailField(max_length=100, null=False, blank=True, verbose_name="email")

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.name


class VerifyCode(models.Model):
    "texo"
    code = models.CharField(max_length=10, verbose_name="verification code")
    mobile = models.CharField(max_length=11, verbose_name="mobile")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="join time")

    class Meta:
        verbose_name = "texto verification code"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
