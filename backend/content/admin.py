from django.contrib import admin

from .models import Module, Topic


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
	list_display = ("title", "order")
	search_fields = ("title",)
	ordering = ("order", "title")


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
	list_display = ("title", "module", "order")
	list_filter = ("module",)
	search_fields = ("title", "body")
	ordering = ("module", "order", "title")
