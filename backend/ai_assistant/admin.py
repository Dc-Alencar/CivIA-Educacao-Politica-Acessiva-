from django.contrib import admin

from .models import InteractionLog


@admin.register(InteractionLog)
class InteractionLogAdmin(admin.ModelAdmin):
	list_display = ("id", "user", "topic", "created_at")
	list_filter = ("topic", "created_at")
	search_fields = ("anon_prompt", "ai_response", "legal_sources", "user__username")
	readonly_fields = ("created_at",)
