from django.db import models

# Create your models here.


class Program(models.Model):
    id = models.AutoField(primary_key=True)
    visible = models.BooleanField(default=True)
    seq = models.CharField(max_length=100, null=False, verbose_name="项目编号")
    name = models.CharField(max_length=500, verbose_name="项目名称", null=False)
    desp = models.CharField(max_length=1000, verbose_name="项目描述", null=True)
    responser = models.CharField(max_length=100, verbose_name="项目负责人", null=False)
    location = models.CharField(max_length=100, verbose_name="所属地", null=True)
    money = models.CharField(max_length=100, null=True,verbose_name="招标金额")

    # date
    program_date = models.DateField(verbose_name="创建时间")
    start_date = models.DateField(verbose_name="评标开始时间")
    end_date = models.DateField(verbose_name="评标截止时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = verbose_name