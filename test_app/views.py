from django.http import JsonResponse
from rest_framework.views import APIView
from .models import TestModel
from django.forms.models import model_to_dict
#from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
class simple(APIView):
    '''
        Cloud-based views
    '''
    def post(self, request):
        # Creating data
        new_test_content = TestModel.objects.create(
            name = request.data["name"],
            description = request.data["description"],
            phone_number = request.data["phone_number"],
            is_alive = request.data["is_alive"],
            amount = request.data["amount"]
        )
        return JsonResponse({"data": model_to_dict(new_test_content)})

    def get(self, request):
        content = TestModel.objects.all().values()
        print(content)
        return JsonResponse({"data": list(content)})