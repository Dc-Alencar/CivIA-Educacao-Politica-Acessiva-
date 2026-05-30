from django.db import models

from .question import Question


class Alternative(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="alternatives")
    text = models.TextField()
    is_correct = models.BooleanField(default=False)

    class Meta:
        ordering = ["question", "-is_correct", "text"]

    def __str__(self):
        return self.text