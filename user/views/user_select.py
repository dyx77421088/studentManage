from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import serializers, mixins, status
from rest_framework.serializers import ModelSerializer

from user.models import User
from rest_framework.response import Response


class UserInfoSerializers2(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserSelectView(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     GenericViewSet):
    """
    list:
    获得所有用户信息

    无描述
    """
    queryset = User.objects.all()
    serializer_class = UserInfoSerializers2

    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset, many=True)
        # Expected type 'str', got 'Dict[str, Union[int, Any]]' instead
        return Response({"code": 200, "data": serializer.data})

    def retrieve_by_username(self, request, *args, **kwargs):
        try:
            instance = self.queryset.get(username=kwargs.get("username"))
        except User.DoesNotExist:
            return Response({"message": "没找到"})
        except User.MultipleObjectsReturned:
            return Response({"message": "返回多个"})
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
