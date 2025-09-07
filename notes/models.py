from django.db import models

# Create your models here.
from django.conf import settings
from core.models import TimeStampedModel
from academic.models import Category, AcademicLevel, Course, Lecturer

from core.models import TimeStampedModel
from django.conf import settings

class Note(TimeStampedModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notes")
    level = models.ForeignKey(AcademicLevel, on_delete=models.SET_NULL, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.CharField(max_length=255, blank=True)  # comma-separated tags/topics
    is_public = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.title


