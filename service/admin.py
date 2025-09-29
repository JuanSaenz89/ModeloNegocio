from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Service, ServiceAdmin)
