from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
	fieldsets = BaseUserAdmin.fieldsets + (
		('Consentimento', {'fields': ('accepted_terms', 'terms_accepted_at')}),
	)
	add_fieldsets = BaseUserAdmin.add_fieldsets + (
		('Consentimento', {'fields': ('accepted_terms', 'terms_accepted_at')}),
	)
	list_display = BaseUserAdmin.list_display + ('accepted_terms', 'terms_accepted_at')
