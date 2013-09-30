from django.contrib import admin
from models import Probe


class ProbeAdmin(admin.ModelAdmin):
    list_display = ['application', 'status', 'probeid', 'responsetime', 'timestamp']


admin.site.register(Probe, ProbeAdmin)