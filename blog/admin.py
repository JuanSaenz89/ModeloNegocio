from django.contrib import admin
from .models import Post, Category
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'post_categories','publish_time', 'created_at')
    list_filter = ('author', 'categories', 'publish_time')
    search_fields = ('title', 'author__username')
    prepopulated_fields = {'title': ('title',)}
    date_hierarchy = 'publish_time'
    ordering = ('-publish_time',)

    def post_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    post_categories.short_description = 'Categories' # type: ignore


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    prepopulated_fields = {'name': ('name',)}
    ordering = ('name',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)