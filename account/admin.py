from unfold.admin import ModelAdmin
from django.contrib import admin
from account.models import Profile

@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    list_display = ("user", "note", "twitter")
    search_fields = ("user__username", "note", "twitter")

    fieldsets = (
        ("User Info", {"fields": ("user", "note", "twitter")}),
    )
