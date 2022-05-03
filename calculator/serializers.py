from pickle import TRUE
from rest_framework import serializers



class RiskSerializer(serializers.Serializer):
    age=serializers.IntegerField(required=True)
    num_biopsy=serializers.IntegerField(required=True)
    menarch_age=serializers.IntegerField(required=True)
    live_birth_age=serializers.IntegerField(required=True)
    ever_had_biopsy=serializers.IntegerField(required=True)
    first_deg_relatives=serializers.IntegerField(required=True)
    ihyp=serializers.IntegerField(required=True)
    race=serializers.IntegerField(required=True)
