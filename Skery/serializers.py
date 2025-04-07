from rest_framework import serializers
from .models import listtodo

class listtodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = listtodo
        fields = ['id', 'title', 'completed']