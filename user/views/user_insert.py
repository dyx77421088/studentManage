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
        fields = ["userName", "password", "phoneNumber"]


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
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
