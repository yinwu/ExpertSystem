from django.db import models

# Create your models here.

from program.models import Program


class Expert(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="专家姓名")
    phone = models.CharField(max_length=100, verbose_name="联系方式")
    email = models.CharField(max_length=100, verbose_name="电子邮箱", null=True)
    address = models.CharField(max_length=100, verbose_name="联系地址", null=True)
    unit = models.CharField(max_length=100, verbose_name="工作单位")


    degree_choice = [
        ("benke","本科"),
        ("shuoshi","硕士"),
        ("boshi","博士"),
        ("boshihou","博士后"),
        ("other","其他")
    ]

    level_choice = [
        ("chuji","初级职称"),
        ("zhongji","中级职称"),
        ("gaoji","高级职称"),
        ("jiaoshou","教授"),
        ("shuodao","硕士生导师"),
        ("bodao","博士生导师"),
        ("yuanshi","院士"),
        ("other","其他类")
    ]

    type_choice = [
        ("ligong","理工类"),
        ("wenshi","文史类"),
        ("yishu","艺术类"),
        ("other","其他")
    ]

    degree = models.CharField(max_length=500, verbose_name="学历", choices=degree_choice, default="other")
    level = models.CharField(max_length=500, verbose_name="职务等级", choices=level_choice, default="other")
    program_type = models.CharField(max_length=500, verbose_name="专业类型", choices=type_choice, default="other")

    selected_program_list = models.ManyToManyField(Program, related_name="selected", through="Comments")
    excluded_program_list = models.ManyToManyField(Program, related_name="excluded", through="ExcluedeExpert")


    class Meta:
        verbose_name = '专家'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class ExcluedeExpert(models.Model):
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE, verbose_name='排除的评审专家')
    program = models.ForeignKey(Program, on_delete=models.CASCADE, verbose_name='排除的项目名称')

class Comments(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, verbose_name='项目名称')
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE, verbose_name='评审专家')
    content = models.CharField(max_length=10000, verbose_name="评审意见")
    input_date = models.DateField(auto_now=True, verbose_name="评审日期")