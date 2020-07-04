from django.contrib import admin





# Register your models here.
from .models import *

admin.site.register(Program)
admin.site.site_header = 'XX大学专家抽签系统'
admin.site.site_title = 'XX大学专家抽签系统'
