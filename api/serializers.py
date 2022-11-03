from rest_framework.serializers import ModelSerializer
from .models import *

class TraineeSerializer(ModelSerializer):
    class Meta:
        model = Trainee
        fields = ["name","technology"]