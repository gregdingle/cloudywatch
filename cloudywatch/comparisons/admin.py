from django.contrib import admin

from .models import Comparison


class ComparisonAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['applications']


admin.site.register(Comparison, ComparisonAdmin)
