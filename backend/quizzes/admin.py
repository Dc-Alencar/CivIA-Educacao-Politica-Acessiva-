from django.contrib import admin

from .models import Alternative, Question, UserAnswer

class AlternativeInline(admin.TabularInline):
	model = Alternative
	extra = 0


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	list_display = ("text", "topic")
	list_filter = ("topic",)
	search_fields = ("text",)
	inlines = [AlternativeInline]


@admin.register(Alternative)
class AlternativeAdmin(admin.ModelAdmin):
	list_display = ("text", "question", "is_correct")
	list_filter = ("is_correct", "question")
	search_fields = ("text", "explanation")

admin.site.register(UserAnswer)