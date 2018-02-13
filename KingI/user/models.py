from django.db import models


# 用户信息表
class user_Info(models.Model):

    user_name  = models.CharField(max_length=32,unique=True,verbose_name="账号") # 姓名 唯一
    def __str__(self):
        return self.user_name
    user_pwd   = models.CharField(max_length=64,verbose_name="密码") # 密码
    gender_type = (
        (1, "男"),
        (2, "女"),
        (3, "空"),
    )
    gender    = models.IntegerField(choices=gender_type,default=3,verbose_name="性别") # 数字分组
    mail      = models.EmailField(max_length=64,null=True,blank=True,verbose_name="邮箱") # 邮箱格式
    marriage  = models.BooleanField(verbose_name="婚姻") # Bool格式

    # group     = models.ForeignKey("userGroup",to_field="group_id", on_delete=models.CASCADE, )  # 外键
