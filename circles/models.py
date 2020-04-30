from django.db import models
from django.utils import timezone

from django.contrib.auth import get_user_model


class Event(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    start = models.DateTimeField("Start-Zeitpunkt")

    host = models.ForeignKey(
        get_user_model(), related_name="hosted_events", on_delete=models.CASCADE
    )
    participants = models.ManyToManyField(get_user_model(), related_name="events")

    @property
    def is_full(self):
        """determines wether event is already full (6 participants, 7 including host)"""
        return self.participants.count() >= 6

    def __str__(self) -> str:
        return str(self.start)

    class Meta:
        ordering = ("start",)