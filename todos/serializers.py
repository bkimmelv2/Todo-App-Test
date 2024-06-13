from .models import Todo
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our Serializer
class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model to be serialized
        model = Todo
        # fields to be included in output
        fields = ['id', 'subject', 'details']