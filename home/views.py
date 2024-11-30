from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    html = "<p>Hello, World!</p>"
    return HttpResponse(html)