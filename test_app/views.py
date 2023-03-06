from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def simple(request):
    # perform opereations
    method = request.method.lower()
    if method == "get":
        return JsonResponse({"data": [1, 3, 4, 4, 5]})
    elif method == "post":
        return JsonResponse({"data": "Added data successfully"})
    elif method == "put":
        return JsonResponse({"data": "Updated data successfully"})
    return JsonResponse({"error": "method not allowed"})
