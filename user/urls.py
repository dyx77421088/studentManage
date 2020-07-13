from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.contrib import admin

from user.views.user_insert import UserInsertView
from user.views.user_other import UserOtherView
from user.views.user_select import UserSelectView

urlpatterns = [
    path("insert", UserInsertView.as_view({'post': 'create'})),

    path("getAll", UserSelectView.as_view({'get': 'list'})),
    path("getUserById/<int:pk>", UserSelectView.as_view({'get': 'retrieve'})),
    path("getUserByuserName/<str:userName>", UserSelectView.as_view({'get': 'retrieve_by_username'})),
    path("login", UserSelectView.as_view({'post': 'login'})),

    path("update/<int:pk>", UserOtherView.as_view({'patch': 'partial_update'})),
    path("delete/<int:pk>", UserOtherView.as_view({'delete': 'destroy'})),
]
