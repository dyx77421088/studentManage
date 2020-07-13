import re

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import serializers, mixins, status
from rest_framework.serializers import ModelSerializer

from user.models import User
from rest_framework.response import Response


class UserInfoSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserInsertView(mixins.CreateModelMixin,
                     GenericViewSet):
    """
    create:
    添加一条数据

    无描述
    """
    queryset = User.objects.all()
    serializer_class = UserInfoSerializers

    # @swagger_auto_schema(
    #     request_body=openapi.Schema(
    #         type=openapi.TYPE_OBJECT,
    #         properties={
    #             'date': openapi.Schema(type=openapi.TYPE_INTEGER, description="这是date"),
    #             'username': openapi.Schema(type=openapi.TYPE_INTEGER),
    #         }
    #     ),
    #     responses={
    #         200: openapi.Schema(
    #             type=openapi.TYPE_OBJECT,
    #             properties={
    #                 'date': openapi.Schema(type=openapi.TYPE_INTEGER, description="这是date"),
    #                 'username': openapi.Schema(type=openapi.TYPE_INTEGER),
    #             }
    #         ),
    #         400: '参数错误',
    #         201: UserInfoSerializers
    #     }
    # )
    def create(self, request, *args, **kwargs):
        if not pd_phone_number(request.data.get("phoneNumber")):
            return Response({"message": "手机号格式错误"})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


def pd_phone_number(phone) -> bool:
    return re.match(r'^1[345678]\d{9}$', phone) is not None
