from django.db import models

# Create your models here.
from user.models import User


class Clazz(models.Model):
    class_name = models.CharField()

    class Meta:
        verbose_name = '班级表'
        verbose_name_plural = verbose_name
