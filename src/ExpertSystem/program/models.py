from django.db import models

# Create your models here.


class Program(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="序号")
    name = models.CharField(max_length=500, verbose_name="项目名称")
    responser = models.CharField(max_length=100, verbose_name="项目负责人")
    program_date = models.DateField(verbose_name="发起时间")
    desp = models.CharField(max_length=1000, verbose_name="项目描述")
