from django.conf import settings
from django.db import models


class InteractionLog(models.Model):
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		related_name="interaction_logs",
	)
	topic = models.ForeignKey("content.Topic", on_delete=models.CASCADE, related_name="interaction_logs")
	anon_prompt = models.TextField()
	ai_response = models.TextField()
	legal_sources = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-created_at"]

	def __str__(self):
		return f"InteractionLog #{self.pk}"
