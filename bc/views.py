from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer


class NoteAPIView(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
