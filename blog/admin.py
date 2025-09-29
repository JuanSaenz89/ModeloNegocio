from django.contrib import admin
from .models import Post, Category
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_time', 'created_at')
    list_filter = ('author', 'categories', 'publish_time')
    search_fields = ('title', 'content')
    prepopulated_fields = {'title': ('title',)}
    date_hierarchy = 'publish_time'
    ordering = ('-publish_time',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    prepopulated_fields = {'name': ('name',)}
    ordering = ('name',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)