from django.urls import path, include
from .views import novoapp

urlpatterns = [
    path('novoapp',novoapp)
]
