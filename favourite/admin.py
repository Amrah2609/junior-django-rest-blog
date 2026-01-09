from unfold.admin import ModelAdmin
from django.contrib import admin
from favourite.models import Favourite

@admin.register(Favourite)
class FavouriteAdmin(ModelAdmin):
    list_display = ("user", "post")
    list_filter = ("user", "post")
    search_fields = ("user__username", "post__title")

    fieldsets = (
        ("Favourite Info", {"fields": ("user", "post"), "classes": ("collapse",)}),
    )
