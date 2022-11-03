from django.urls import path
from .views import *
urlpatterns = [
    path("",TraineeCreate.as_view(),name="create_trainee")
]