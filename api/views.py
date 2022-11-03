from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import *

class TraineeCreate(ListCreateAPIView):
    serializer_class = TraineeSerializer
    queryset = Trainee.objects.all()



# Create your views here.
