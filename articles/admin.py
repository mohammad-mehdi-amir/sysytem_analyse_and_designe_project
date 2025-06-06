
from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'is_active', 'datetime_add']
    list_filter = ['status', 'is_active', 'datetime_add']
    search_fields = ['title', 'text', 'author__username']