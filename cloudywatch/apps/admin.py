from django.contrib import admin
from models import Category, Application


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'pingdom_id']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Application, ApplicationAdmin)