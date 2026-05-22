from django.db import models


class Question(models.Model):
    topic = models.ForeignKey("content.Topic", on_delete=models.CASCADE, related_name="questions")
    text = models.TextField()

    class Meta:
        ordering = ["topic", "text"]

    def __str__(self):
        return self.text