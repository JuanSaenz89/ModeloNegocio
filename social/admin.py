from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from .models import Link


# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'created_at', 'updated_at')
    search_fields = ('name', 'url', 'key')
    list_filter = ('created_at', 'updated_at')
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    prepopulated_fields = {'key': ('name',)}

    def get_readonly_fields(self, request: HttpRequest, obj: Any | None = ...) -> list[str] | tuple[Any, ...]:
        if request.user.groups.filter(name='Content Editors').exists():
            return ('created_at', 'updated_at', 'key', 'name')
        return super().get_readonly_fields(request, obj)

admin.site.register(Link, LinkAdmin)