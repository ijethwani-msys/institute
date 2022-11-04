from rest_framework.serializers import ModelSerializer
from .models import *

class TraineeSerializer(ModelSerializer):
    class Meta:
        model = Trainee
        fields = ["name","technology"]

class TrainerSerializer(ModelSerializer):
    class Meta:
        model = Trainer
        fields = ["name","technology"]

class TrainingSerializer(ModelSerializer):
    class Meta:
        model = Training
        fields = ["name_of_training","duration","trainer","trainee","start_date"]