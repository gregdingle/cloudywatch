from django.contrib import admin

from .forms import ComparisonForm
from .models import Comparison


class ComparisonAdmin(admin.ModelAdmin):
    form = ComparisonForm
    list_display = ['title', 'slug']
    filter_horizontal = ['applications']


admin.site.register(Comparison, ComparisonAdmin)
