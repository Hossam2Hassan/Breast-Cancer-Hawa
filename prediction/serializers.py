from rest_framework import serializers
from .models import prediction


class predictionSerializers(serializers.ModelSerializer):
    perimeter_mean=serializers.DecimalField(max_digits=10, decimal_places=5,required=True)
    area_mean=serializers.DecimalField(max_digits=10, decimal_places=5,required=True)
    area_se=serializers.DecimalField(max_digits=10, decimal_places=5,required=True)
    perimeter_worst=serializers.DecimalField(max_digits=10, decimal_places=5,required=True)
    area_worst=serializers.DecimalField(max_digits=10, decimal_places=5,required=True)
    class Meta:
        model = prediction
        fields = ['perimeter_mean','area_mean','area_se','perimeter_worst','area_worst','result']
    # def save(self,**kwargs):
        
    #     data= prediction(
    #         user = self.context['request'].user,
    #         perimeter_mean=self.validated_data['perimeter_mean'],
    #         area_mean=self.validated_data['area_mean'],
    #         area_se=self.validated_data['area_se'],
    #         perimeter_worst=self.validated_data['perimeter_worst'],
    #         area_worst=self.validated_data['area_worst']
    #     )
    #     data.save()
    #     return data

