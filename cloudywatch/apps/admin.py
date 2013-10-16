from django.contrib import admin
from models import Category, Application


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'pingdom_id', 'downtime']
    readonly_fields = ['downtime']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Application, ApplicationAdmin)
