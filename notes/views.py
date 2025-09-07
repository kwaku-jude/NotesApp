from django.db import models
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, viewsets, status
from rest_framework.response import Response

from .models import Note
from .serializers import NoteSerializer
from django.db.models import Q


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: Only owners can edit; others can read if public.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions for public notes
        if request.method in permissions.SAFE_METHODS:
            return obj.is_public or obj.owner == request.user
        # Write permissions only for owner
        return obj.owner == request.user

# List and create notes
class NoteListCreateView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Note.objects.filter(Q(owner=self.request.user) | Q(is_public=True))
        params = self.request.query_params
        if level := params.get('level'):
            queryset = queryset.filter(level__name__iexact=level)
        if course := params.get('course'):
            queryset = queryset.filter(course__name__iexact=course)
        if lecturer := params.get('lecturer'):
            queryset = queryset.filter(lecturer__name__iexact=lecturer)
        if tags := params.get('tags'):
            tag_list = [t.strip().lower() for t in tags.split(',')]
            queryset = queryset.filter(
                Q(tags__iregex=r'(' + '|'.join(tag_list) + r')')
            )
        if search := params.get('search'):
            queryset = queryset.filter(Q(title__icontains=search) | Q(content__icontains=search))
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Retrieve, update, delete note
class NoteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        title = instance.title  # keep the note title for the message
        self.perform_destroy(instance)
        return Response(
            {"message": f"Note '{title}' has been deleted successfully."},
            status=status.HTTP_200_OK
        )
