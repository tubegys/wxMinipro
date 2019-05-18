from django.db import models


# Create your models here.


class UserMessage(models.Model):
    # object_id = models.CharField(primary_key=True, verbose_name="主键", max_length=20, default="")
    name = models.CharField(max_length=20, verbose_name="用户名", default="", blank=True, null=True)
    email = models.EmailField(verbose_name="邮箱")
    address = models.CharField(max_length=100, verbose_name="联系地址")
    message = models.CharField(max_length=500, verbose_name="留言信息")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "用户留言信息"
        verbose_name_plural = verbose_name
        db_table = "user_message"
        # ordering = ["-object_id", ]  # 倒序
