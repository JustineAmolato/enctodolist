from django.shortcuts import render
from rest_framework import viewsets
from .models import listtodo
from .serializers import listtodoSerializer

class listtodoViewSet(viewsets.ModelViewSet):
    queryset = listtodo.objects.all()
    serializer_class = listtodoSerializer