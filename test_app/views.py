from django.http import JsonResponse
from rest_framework import generics
from .models import TestModel
from .serializers import SimpleSerializer

class SimpleGenerics(generics.ListCreateAPIView):
    ''' Creates data '''
    queryset = TestModel.objects.all()
    serializer_class = SimpleSerializer

class SimpleGenericsUpdate(generics.UpdateAPIView):
    ''' Updates data '''
    queryset = TestModel.objects.all()
    serializer_class = SimpleSerializer
    lookup_field = "id"