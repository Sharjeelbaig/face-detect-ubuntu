from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils.base64recognition import base64recognition as b64r
import json

# Create your views here.
@csrf_exempt
def detectface(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        string1 = data.get('string1')
        string2 = data.get('string2')
        output = b64r(string1, string2)
        
        return JsonResponse({'output': output})
    