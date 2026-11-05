
from django.contrib import admin

from .models import Article, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "category",
        "author",
        "status",
        "published_at",
    ]

    list_filter = ["status", "category", "published_at"]

    search_fields = ["title", "body"]

    prepopulated_fields = {"slug": ("title",)}

    date_hierarchy = "published_at"

    ordering = ["-published_at"]
