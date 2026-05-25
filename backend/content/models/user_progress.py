from django.db import models
from django.conf import settings

from .topic import Topic

class UserProgress(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
    )
    
    completed = models.BooleanField(
        default=False   
    )

    completed_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ("user", "topic")
        
    def __str__(self):

        return f"{self.user.username} - {self.topic.title}"