from django.contrib import admin

# Register your models here.
from .models import Expert, Comments

admin.site.register(Expert)
admin.site.register(Comments)
