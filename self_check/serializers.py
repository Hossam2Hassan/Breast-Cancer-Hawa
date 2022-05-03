from rest_framework import serializers
from authentication.models import User
from . import models
from datetime import timedelta

class Self_checkSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Self_checkModel
        fields=['id','question']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.CheckingModel
        fields=['answer','self_check','date']
        depth = 1


class CalenderSerializer(serializers.ModelSerializer):
    period=serializers.CharField(required=True)
    class Meta:
        model=models.CalendarModel
        fields=['period','self_check']