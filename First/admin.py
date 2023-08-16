from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import Group
from .models import *
class PostAdmin(ModelAdmin):
    list_display = ['title','body','Completed']
    list_filter = ['Completed']
admin.site.register(Todo,PostAdmin)
# Register your models here.
admin.site.unregister(Group)