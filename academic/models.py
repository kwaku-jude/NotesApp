from django.db import models

# Create your models here.
from core.models import TimeStampedModel

class Category(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

from django.db import models

class AcademicLevel(models.Model):
    name = models.CharField(max_length=50, unique=True)  # e.g., Freshman, Sophomore

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    level = models.ForeignKey(AcademicLevel, on_delete=models.CASCADE, related_name="courses")

    def __str__(self):
        return f"{self.name} ({self.level.name})"

class Lecturer(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course, related_name="lecturers")

    def __str__(self):
        return self.name
