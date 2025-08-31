from rest_framework import serializers
from .models import Note
from academic.models import Category

class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    category = serializers.CharField(
        required=False, allow_blank=True, allow_null=True
    )

    class Meta:
        model = Note
        fields = [
            "id",
            "title",
            "content",
            "owner",
            "category",
            "is_public",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        category_name = validated_data.pop('category', None)
        if category_name:
            category_obj, _ = Category.objects.get_or_create(name=category_name)
            validated_data['category'] = category_obj
        else:
            validated_data['category'] = None
        return super().create(validated_data)

    def validate_category(self, value):
        if value:
            return value.strip().title()  # Capitalize properly
        return None

    def update(self, instance, validated_data):
        category_name = validated_data.pop('category', None)
        if category_name is not None:
            category_obj, _ = Category.objects.get_or_create(name=category_name)
            validated_data['category'] = category_obj
        return super().update(instance, validated_data)
