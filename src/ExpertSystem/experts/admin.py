from django.contrib import admin

# Register your models here.
from .models import Expert, Comments, ExcluedeExpert

admin.site.register(Expert)
admin.site.register(Comments)
admin.site.register(ExcluedeExpert)