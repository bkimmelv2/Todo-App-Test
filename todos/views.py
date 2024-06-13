from django.shortcuts import render
from .models import Todo
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer

# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    # The main query for Index Route
    queryset = Todo.objects.all()
    # Serializer class for serialized output
    serializer_class = TodoSerializer
    # optional permission class to set permission level
    permission_classes = [permissions.AllowAny] # Could instead be [permissions.IsAuthenticated] for example