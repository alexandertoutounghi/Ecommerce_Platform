# -*- coding: utf-8 -*-
from thestars.settings import REGEX_MOBILE

__author__ = 'bobby'
import re
from rest_framework import serializers
from django.contrib.auth import get_user_model
from datetime import datetime
from datetime import timedelta
from rest_framework.validators import UniqueValidator

from .models import VerifyCode

User = get_user_model()


class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self, mobile):
        """
        Validate mobile
        :param data:
        :return:
        """

        # Mobile number already exists?
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("User already exists")

        # valid mobile number?
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("Illegal phone number")

        # Verification code sending frequency
        one_mintes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_mintes_ago, mobile=mobile).count():
            raise serializers.ValidationError("距离上一次发送未超过60s")

        return mobile


class UserDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for user detail
    """

    class Meta:
        model = User
        fields = ("name", "gender", "birthday", "email", "mobile")


class UserRegSerializer(serializers.ModelSerializer):
    code = serializers.CharField(required=True, write_only=True, max_length=4, min_length=4, label="Verification code",
                                 error_messages={
                                     "blank": "Please input verification code",
                                     "required": "Please input verification code",
                                     "max_length": "Invalid verification code format",
                                     "min_length": "Invalid verification code format"
                                 },
                                 help_text="Verification Code")
    username = serializers.CharField(label="Username", help_text="Username", required=True, allow_blank=False,
                                     validators=[
                                         UniqueValidator(queryset=User.objects.all(), message="User already exists")])

    password = serializers.CharField(
        style={'input_type': 'password'}, help_text="password", label="password", write_only=True,
    )

    # def create(self, validated_data):
    #     user = super(UserRegSerializer, self).create(validated_data=validated_data)
    #     user.set_password(validated_data["password"])
    #     user.save()
    #     return user

    def validate_code(self, code):
        # try:
        #     verify_records = VerifyCode.objects.get(mobile=self.initial_data["username"], code=code)
        # except VerifyCode.DoesNotExist as e:
        #     pass
        # except VerifyCode.MultipleObjectsReturned as e:
        #     pass
        verify_records = VerifyCode.objects.filter(mobile=self.initial_data["username"]).order_by("-add_time")
        # if verify_records:
        #     last_record = verify_records[0]

        #     five_mintes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
        #     if five_mintes_ago > last_record.add_time:
        #         raise serializers.ValidationError("Verification Code Expired")

        #     if last_record.code != code:
        #         raise serializers.ValidationError("Invalid verification code")

        # else:
        #     raise serializers.ValidationError("Invalid verification code")

    def validate(self, attrs):
        attrs["mobile"] = attrs["username"]
        del attrs["code"]
        return attrs

    class Meta:
        model = User
        fields = ("username", "code", "mobile", "password")
