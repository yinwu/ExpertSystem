from django.contrib import admin





# Register your models here.
from .models import *

admin.site.register(Program)
admin.site.site_header = '专家抽取系统后台管理系统'
admin.site.site_title = '陆军防化指挥工程学院专专家抽取系统'
