from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def hello(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'Hello, World!'}, status=200)
    else:
        return JsonResponse({'message': 'Method Not Allowed'}, status=405)
