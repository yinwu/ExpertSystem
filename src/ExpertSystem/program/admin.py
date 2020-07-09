from django.contrib import admin





# Register your models here.
from .models import *

admin.site.register(Program)
admin.site.site_header = '陆军防化指挥工程学院专家抽取系统'
admin.site.site_title = '陆军防化指挥工程学院专专家抽取系统'
