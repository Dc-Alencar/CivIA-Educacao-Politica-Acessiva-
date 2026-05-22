from django.db import models

from .module import Module


class Topic(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="topics")
    title = models.CharField(max_length=255)
    body = models.TextField()
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ["module", "order", "title"]

    def __str__(self):
        return self.title