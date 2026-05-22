from django.db import models


class Module(models.Model):
	title = models.CharField(max_length=255)
	order = models.PositiveIntegerField()

	class Meta:
		ordering = ["order", "title"]

	def __str__(self):
		return self.title
