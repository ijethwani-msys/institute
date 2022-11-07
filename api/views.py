from rest_framework.generics import *
from .serializers import *
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

#__________________________________________________Trainee
class TraineeCreate(CreateAPIView):
    """Create Trainee"""
    serializer_class = TraineeSerializer
    queryset = Trainee.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    def get(self, request, *args, **kwargs):
        return Response(template_name='index.html')
    



class TraineeList(ListAPIView):
    """List Of Trainee"""
    serializer_class = TraineeSerializer
    queryset = Trainee.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    def get(self, request, *args, **kwargs):
        return Response({"data":self.get_queryset(),"table_headers":["ID","Name","Technology","DOJ","Status"]},template_name='index.html')


class TraineeDetail(RetrieveUpdateDestroyAPIView):
    """Details Of Trainee"""
    serializer_class = TraineeSerializer
    queryset = Trainee.objects.all()
    lookup_field = "pk"

#_________________________________________________________________________Trainer
class TrainerCreate(CreateAPIView):
    """Create Trainer"""
    serializer_class = TrainerSerializer
    queryset = Trainer.objects.all()

class TrainerList(ListAPIView):
    """List Of Trainer"""
    serializer_class = TrainerSerializer
    queryset = Trainer.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    def get(self, request, *args, **kwargs):
        return Response({"data":self.get_queryset(),"table_headers":["ID","Name","Technology","DOJ","Status"]},template_name='index.html')



class TrainerDetail(RetrieveUpdateDestroyAPIView):
    """Trainer Details"""
    serializer_class = TrainerSerializer
    queryset = Trainer.objects.all()
    lookup_field = "pk"

#_________________________________________________________________________Traineing

class TrainingCreate(CreateAPIView):
    """Create Training"""
    serializer_class = TrainingSerializer
    queryset = Training.objects.all()
class TrainingList(ListAPIView):
    """List Of Training"""
    serializer_class = TrainingSerializer
    queryset = Training.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    def get(self, request, *args, **kwargs):
        return Response({"data":self.get_queryset(),"table_headers":["ID","Name","Duration","Trainer","Start Date"],"type":"training_list"},template_name='index.html')

class TrainingDetail(RetrieveUpdateDestroyAPIView):
    """Training Details"""
    serializer_class = TrainingSerializer
    queryset = Training.objects.all()
    lookup_field = "pk"



