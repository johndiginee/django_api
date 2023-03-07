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
        serializer.save()
        return JsonResponse({"data": serializer.data})

    def get(self, request):
        content = TestModel.objects.all()
        return JsonResponse({"data": SimpleSerializer(content, many=True).data})

    def put(self, request, *args, **kwargs):
        model_id = kwargs.get("id", None)
        if not model_id:
            return JsonResponse({"error": "method /PUT/ not allowed"})
        
        try:
            instance = TestModel.objects.get(id=model_id)
        except:
            JsonResponse({"error": "Object does not exist"})
        
        serializer = SimpleSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({"data": serializer.data})