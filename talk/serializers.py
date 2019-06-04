from rest_framework import serializers

from talk.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name', 'speaker', 'venue', 'duration')