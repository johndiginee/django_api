from django.http import JsonResponse
from rest_framework import generics
from .models import TestModel
from .serializers import SimpleSerializer
from rest_framework import viewsets

class SimpleViewset(viewsets.ModelViewSet):
    # API endpoint for listing, updating and creating data.
    queryset = TestModel.objects.all()
    serializer_class = SimpleSerializer
