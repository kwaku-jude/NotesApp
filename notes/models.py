from django.db import models

# Create your models here.
from django.conf import settings
from core.models import TimeStampedModel
from academic.models import Category

class Note(TimeStampedModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notes"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="notes"
    )
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.title

