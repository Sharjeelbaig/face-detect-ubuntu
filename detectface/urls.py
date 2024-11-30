from django.urls import path
from . import views

urlpatterns = [
    path('detectface/', views.detectface, name='detectface'),
]