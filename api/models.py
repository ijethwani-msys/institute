from email.policy import default
from django.db import models

# Created at 2/11/2022 11:28 

# one to one
# many to one (Forginkey)
# many to many
class Trainer(models.Model):
    """It Contains Objects of Trainer"""
    name = models.CharField(max_length=100,verbose_name="Trainer Name",blank=True,null=True)
    technology = models.CharField(max_length=50,verbose_name="Technology Name",blank=True,null=True)
    joined_at = models.DateTimeField(auto_now_add=True,verbose_name="Date Of Joining")

    def __str__(self):
        return self.name
    class Meta:
        ordering = ["-joined_at"]

class Trainee(models.Model):
    """It Contains Objects of  Trainee"""
    name = models.CharField(verbose_name="Name Of Trainee",max_length=100,blank=True,null=True)
    technology = models.CharField(max_length=50,verbose_name="Technology Name",blank=True,null=True)
    joined_at = models.DateTimeField(auto_now_add=True,verbose_name="Date Of Joining")

    def __str__(self):
        return self.name
    class Meta:
        ordering = ["-joined_at"]


class Training(models.Model):
    """It contains Objects Of Training"""
    name_of_training = models.CharField(max_length=100,verbose_name="Training Name",blank=True,null=True)
    duration = models.PositiveIntegerField(default=1,verbose_name="Duration In Months")
    trainer = models.ForeignKey("trainer",on_delete=models.CASCADE,verbose_name="Trainer")
    trainee = models.ForeignKey("trainee",on_delete=models.SET_NULL,verbose_name="Trainee",null=True)
    start_date = models.DateField(blank=True,null=True,verbose_name="Start Date")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Created At")

    def __str__(self):
        return self.name_of_training
    class Meta:
        ordering = ["-created_at"]
    





