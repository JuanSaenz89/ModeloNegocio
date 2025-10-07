from django.contrib import admin
from .models import Page
# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    search_fields = ('title',)
    ordering = ('title',)

admin.site.register(Page, PageAdmin)