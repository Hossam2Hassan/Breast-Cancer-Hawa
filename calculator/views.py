from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RiskSerializer
from .import gail
import numpy as np
from django.http import JsonResponse

from .RiskAssessment import BasicRiskAssessment as assessment

class RiskView(generics.GenericAPIView):  
    # authentication_classes = ()
    permission_classes = (IsAuthenticated,)
    serializer_class =RiskSerializer
    def post(self , request , *args , **kwargs):
        serializer = self.get_serializer(data =request.data)
        serializer.is_valid(raise_exception=True)
        age_indicator = 0 if int(request.data['age']) < 50 else 1
        rhyp = np.float64(1.0)
        if request.data['ever_had_biopsy'] == 1:
            if request.data['ihyp'] == 0:
                rhyp = np.float64(0.93)
            elif request.data['ihyp'] == 1:
                rhyp = np.float(1.82)   
        model = gail.GailRiskCalculator()
        model.Initialize()
        fiveyearABS= model.CalculateAbsoluteRisk(
        int(request.data.get('age')),
        int(request.data.get('age')) + 5,
        age_indicator,
        
        int(request.data.get('num_biopsy')),
        int(request.data.get('menarch_age')),
        int(request.data.get('live_birth_age')),
        int(request.data.get('ever_had_biopsy')),
        int(request.data.get('first_deg_relatives')),
        int(request.data.get('ihyp')),
        rhyp,
        int(request.data.get('race'))
        )
        
        fiveYearAVE = model.CalculateAeverageRisk(
        int(request.data.get('age')),
        int(request.data.get('age')) + 5,
        age_indicator,
        
        int(request.data.get('num_biopsy')),
        int(request.data.get('menarch_age')),
        int(request.data.get('live_birth_age')),
        int(request.data.get('ever_had_biopsy')),
        int(request.data.get('first_deg_relatives')),
        int(request.data.get('ihyp')),
        rhyp,
        int(request.data.get('race'))
        )
        
        lifetimeABS = model.CalculateAbsoluteRisk(
        int(request.data.get('age')),
        90,
        age_indicator,
        
        int(request.data.get('num_biopsy')),
        int(request.data.get('menarch_age')),
        int(request.data.get('live_birth_age')),
        int(request.data.get('ever_had_biopsy')),
        int(request.data.get('first_deg_relatives')),
        int(request.data.get('ihyp')),
        rhyp,
        int(request.data.get('race'))
        )
        
        lifetimeAve = model.CalculateAeverageRisk(
        int(request.data.get('age')),
        90,
        age_indicator,
        
        int(request.data.get('num_biopsy')),
        int(request.data.get('menarch_age')),
        int(request.data.get('live_birth_age')),
        int(request.data.get('ever_had_biopsy')),
        int(request.data.get('first_deg_relatives')),
        int(request.data.get('ihyp')),
        int(rhyp),
        int(request.data.get('race'))
        )
        results = assessment()
        results.setRiskScores(fiveyearABS,fiveYearAVE,lifetimeABS,lifetimeAve)
        name= results.getJson()
        

        return Response({"data":name},status=status.HTTP_200_OK)

