from django.shortcuts import render
from rest_framework import generics
from .serializer import ResultSerializer
from .models import Result
# Create your views here.


class ProblemView(generics.CreateAPIView):
    i=Result.objects.all()
    serializer_class=ResultSerializer
