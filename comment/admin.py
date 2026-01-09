from unfold.admin import ModelAdmin
from django.contrib import admin
from comment.models import Comment

@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ("post", "author", "created_at")
    list_filter = ("author", "post", "created_at")
    search_fields = ("content",)

    fieldsets = (
        ("Comment Məlumatı", {"fields": ("post", "content")}),
        ("Author & Meta", {"fields": ("author",), "classes": ("collapse",)}),
    )
