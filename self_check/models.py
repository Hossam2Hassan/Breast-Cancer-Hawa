from django.db import models
from authentication.models import User
# Create your models here.

class Self_checkModel(models.Model):
    question=models.CharField(max_length=50)
    def __str__(self):
        return self.question

class CheckingModel(models.Model):
    self_check=models.ForeignKey(Self_checkModel, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    answer=models.BooleanField(default=False)
    date=models.DateField(auto_now_add=True)

class CalendarModel(models.Model):
    period=models.DateField()
    self_check=models.ForeignKey(User, on_delete=models.CASCADE, null=True)