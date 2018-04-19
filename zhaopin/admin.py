from django.contrib import admin

# Register your models here.
from .models import Zhaopin, WorkLocation, Category


# class ZhaopinAdmin(admin.ModelAdmin):
#     list_display = ['title', 'content', 'peopleNumber', 'workLocation', 'publishTime','category']


admin.site.register(Zhaopin)
admin.site.register(WorkLocation)
admin.site.register(Category)
