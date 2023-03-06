from django.http import JsonResponse
from rest_framework.views import APIView
from .models import TestModel
from .serializers import SimpleSerializer
#from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
class Simple(APIView):
    '''
        Cloud-based views
    '''
    def post(self, request):
        ''' Validating data using Serializer '''
        serializer = SimpleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        ''' Creating data '''
        new_test_content = TestModel.objects.create(
            name = request.data["name"],
            description = request.data["description"],
            phone_number = request.data["phone_number"],
            is_alive = request.data["is_alive"],
            amount = request.data["amount"]
        )
        return JsonResponse({"data": SimpleSerializer(new_test_content).data})

    def get(self, request):
        content = TestModel.objects.all()
        return JsonResponse({"data": SimpleSerializer(content, many=True).data})