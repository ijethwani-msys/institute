from rest_framework.generics import *
from .serializers import *
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import status
from django.shortcuts import redirect

#__________________________________________________Trainee
class TraineeCreate(CreateAPIView):
    """Create Trainee"""
    serializer_class = TraineeSerializer
    queryset = Trainee.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    def post(self,request):
        print(request.data)
        name = request.data["name"]
        technology = request.data["technology"]
        print(name,technology)
        object = Trainee.objects.create(name=name,technology=technology,status=True)
        # seriliaze = self.serializer_class(object)
        return redirect("list_trainee")
    
    



class TraineeList(ListAPIView):
    """List Of Trainee"""
    serializer_class = TraineeSerializer
    queryset = Trainee.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    def get(self, request, *args, **kwargs):
        return Response({"data":self.get_queryset(),"table_headers":["ID","Name","Technology","DOJ","Status"],"button_name":"Add Trainee"},template_name='index.html')
    def post(self,request):
        print(request.data)
        name = request.data["name"]
        technology = request.data["technology"]
        print(name,technology)
        object = Trainee.objects.create(name=name,technology=technology,status=True)
        # seriliaze = self.serializer_class(object)
        return redirect("list_trainee")

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
    def post(self,request):
        print(request.data)
        name = request.data["name"]
        technology = request.data["technology"]
        print(name,technology)
        object = Trainer.objects.create(name=name,technology=technology,status=True)
        # seriliaze = self.serializer_class(object)
        return redirect("list_trainer")


class TrainerList(ListAPIView):
    """List Of Trainer"""
    serializer_class = TrainerSerializer
    queryset = Trainer.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    def get(self, request, *args, **kwargs):
        return Response({"data":self.get_queryset(),"table_headers":["ID","Name","Technology","DOJ","Status"],"button_name":"Add Trainer"},template_name='index.html')
    def post(self,request):
        print(request.data)
        name = request.data["name"]
        technology = request.data["technology"]
        print(name,technology)
        object = Trainer.objects.create(name=name,technology=technology,status=True)
        # seriliaze = self.serializer_class(object)
        return redirect("list_trainer")


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
        return Response({"data":self.get_queryset(),"table_headers":["ID","Name","Duration","Trainer","Start Date"],"type":"training_list","button_name":"Add Training"},template_name='index.html')

class TrainingDetail(RetrieveUpdateDestroyAPIView):
    """Training Details"""
    serializer_class = TrainingSerializer
    queryset = Training.objects.all()
    lookup_field = "pk"



