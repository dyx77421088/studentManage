from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import serializers, mixins, status
from rest_framework.serializers import ModelSerializer

from user.models import User
from rest_framework.response import Response


# class UserInfoSerializers3(ModelSerializer):
#     class Meta:
#         model = User
#         fields = "__all__"
from user.views.user_select import UserInfoSerializers2


class UserOtherView(ModelViewSet):
    """
    update:
    修改用户信息

    无描述
    """
    queryset = User.objects.all()
    serializer_class = UserInfoSerializers2
