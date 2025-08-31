from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

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
