from django.db import models


class DateFields(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        auto_now_add=True, help_text="Date and time created."
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Date and time last updated.",
    )


class Devotional(DateFields):
    title = models.CharField(
        max_length=200,
        help_text="Short title of the devotional",
        blank=True,
    )
    verse_reference = models.CharField(
        max_length=100, help_text="e.g., Exodus 20:1–2, 1 John 5:3"
    )
    scripture_text = models.TextField()
    reflection = models.TextField()

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} ({self.created_at.date()})"
