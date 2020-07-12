from django.urls import path, re_path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.contrib import admin

from user.views.user_insert import UserInsertView

urlpatterns = [
    path("insert", UserInsertView.as_view({'post', 'create'}))
]
