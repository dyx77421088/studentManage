from django.db import models


# Create your models here.
class User(models.Model):
    userName = models.CharField("用户名", max_length=255)
    password = models.CharField("密码", max_length=255)
    phoneNumber = models.CharField("手机号", max_length=255)

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'用户名:{self.userName}, 密码:{self.password}, phoneNumber={self.phoneNumber}'
