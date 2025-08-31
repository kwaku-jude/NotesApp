from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description", "created_at", "updated_at"]


from .models import Note, AcademicLevel, Course, Lecturer

class AcademicLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicLevel
        fields = ['id', 'name']

class CourseSerializer(serializers.ModelSerializer):
    level = AcademicLevelSerializer(read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'level']

class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ['id', 'name']

class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    level = serializers.SlugRelatedField(queryset=AcademicLevel.objects.all(), slug_field='name', required=False, allow_null=True)
    course = serializers.SlugRelatedField(queryset=Course.objects.all(), slug_field='name', required=False, allow_null=True)
    lecturer = serializers.SlugRelatedField(queryset=Lecturer.objects.all(), slug_field='name', required=False, allow_null=True)

    class Meta:
        model = Note
        fields = [
            'id', 'title', 'content', 'owner', 'level', 'course', 'lecturer',
            'tags', 'is_public', 'created_at', 'updated_at'
        ]