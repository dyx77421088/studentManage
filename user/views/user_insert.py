from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import serializers, mixins
from rest_framework.serializers import ModelSerializer

from user.models import User


class UserInfoSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ["userName", "phoneNumber"]


class UserInsertView(mixins.CreateModelMixin,
                     GenericViewSet):
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
        return super().create(request, *args, **kwargs)
