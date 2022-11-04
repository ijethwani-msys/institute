from django.urls import path
from .views import *
urlpatterns = [
    path("trainee_create/",TraineeCreate.as_view(),name="create_trainee"),
    path("trainer_create/",TrainerCreate.as_view(),name="create_trainer"),
    path("training_create/",TrainingCreate.as_view(),name="create_training"),
    path("trainee_list/",TraineeList.as_view(),name="list_trainee"),
    path("trainer_list/",TrainerList.as_view(),name="list_trainer"),
    path("training_list/",TrainingList.as_view(),name="list_training"),
    path("trainee_details/<pk>/",TraineeDetail.as_view(),name="details_trainee"),
    path("trainer_details/<pk>/",TrainerDetail.as_view(),name="details_trainer"),
    path("training_details/<pk>/",TrainingDetail.as_view(),name="details_training")
]