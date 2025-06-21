from django.contrib import admin

from .models import Devotional


@admin.register(Devotional)
class DevotionalAdmin(admin.ModelAdmin):
    list_display = ("title", "verse_reference", "created_at", "updated_at")
    search_fields = ("title", "verse_reference", "scripture_text", "reflection")
    list_filter = ("created_at",)
