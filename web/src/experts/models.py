from django.db import models

# Create your models here.

from program.models import Program
from django.contrib.auth.models import User

def get_default_user():
    return User.objects.get_or_create(id = 2)[0].id

class Expert(models.Model):
    id = models.AutoField(primary_key=True)
    visible = models.BooleanField(default=True, null=True)
    name = models.CharField(max_length=100, verbose_name="专家姓名")
    phone = models.CharField(max_length=100, verbose_name="联系方式")
    email = models.CharField(max_length=100, verbose_name="电子邮箱", null=True)
    address = models.CharField(max_length=100, verbose_name="联系地址", null=True)
    unit = models.CharField(max_length=100, verbose_name="工作单位")

    degree = models.CharField(max_length=500, verbose_name="学历",  null=True)
    level = models.CharField(max_length=500, verbose_name="职务等级", null=True)
    program_type = models.CharField(max_length=500, verbose_name="专业类型", null=True)

    selected_program_list = models.ManyToManyField(Program, related_name="selected", through="Comments")
    account = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="账户", default=get_default_user, null=True)
    class Meta:
        verbose_name = '专家'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Comments(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, verbose_name='项目名称')
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE, verbose_name='评审专家')
    content = models.CharField(max_length=10000, verbose_name="评审意见", null=True)
    input_date = models.DateField(auto_now=True, verbose_name="评审日期")

    status_choice = [
        ("ok","已确认"),
        ("nok","已排除"),
        ("unknow","待确认"),
    ]
 
    valuation_status_choice = [
        ("pass","评审通过"),
        ("nopass","评审不通过"),
        ("unvaluated","待评审"),
    ]
    
    status = models.CharField(max_length=20, verbose_name="确认状态", choices=status_choice, default="unknow", null=True)
    valuation_status = models.CharField(max_length=20, verbose_name="评审状态", choices=valuation_status_choice, default="unvaluated", null=True)
    

    class Meta:
        verbose_name = '专家评审意见'
        verbose_name_plural = verbose_name