from unfold.admin import ModelAdmin
from django.contrib import admin
from post.models import Post
from post.api.permissions import IsAuthorOrReadOnly  
@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ("title", "author", "is_draft", "created_at")
    list_filter = ("is_draft", "author", "created_at")
    search_fields = ("title", "content")

    fieldsets = (
        ("Əsas Məlumat", {"fields": ("title", "content")}),
        ("Status və Permissions", {"fields": ("is_draft", "author"), "classes": ("collapse",)}),
    )
