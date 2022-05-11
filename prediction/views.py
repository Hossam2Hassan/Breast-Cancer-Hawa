from rest_framework import generics,status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import pickle
import numpy as np
from .serializers import predictionSerializers



class PredictionkView(generics.GenericAPIView):  
    # authentication_classes = ()
    permission_classes = (IsAuthenticated,)
    serializer_class =predictionSerializers
    def post(self , request , *args , **kwargs):
        serializer = self.get_serializer(data =request.data)
        serializer.is_valid(raise_exception=True)
        try:
            
            filename="hawa_prediction_model.sav"

            loaded_model = pickle.load(open(filename, 'rb'))
            data = request.data
            values = np.array(list(data.values()))
            print(values)
            values = values.reshape(1, -1)
            print(values)
            print(request.user)
            y_pred = loaded_model.predict(values)
            serializer.save(user=self.request.user , result=y_pred[0])
            print(y_pred[0])
            if y_pred[0] =='B' :
                y_pred='حميد'
                return Response({'status':True,'data':' نتيجه التحليل (ورم  {})'.format(y_pred)})
            elif y_pred[0] =='M':
                y_pred='خبيث'
                return Response({'status':True,'data':' نتيجه التحليل (ورم  {})'.format(y_pred)})
        except ValueError as e:
            return Response(e.args[0], status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def prediction11(request):
    try:
        filename="finalized_model.sav"

        loaded_model = pickle.load(open(filename, 'rb'))
        data=request.data
        print(data)
        unit = np.array(list(data.values()))
        print(unit)
        unit = unit.reshape(1, -1)
        print(unit)
        y_pred = loaded_model.predict(unit)
        return JsonResponse({'status':True,'data':' Result is {}'.format(y_pred)})
    except ValueError as e:
        return Response(e.args[0], status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def prediction(request):
#     try:
#         filename="hawa_prediction_model.sav"

#         loaded_model = pickle.load(open(filename, 'rb'))
#         data=request.data
#         print(data)
#         values = np.array(list(data.values()))
#         print(values)
#         values = values.reshape(1, -1)
#         print(values)
#         y_pred = loaded_model.predict(values)
#         return JsonResponse({'status':True,'data':' Result is {}'.format(y_pred)}, safe=False)
#     except ValueError as e:
#         return Response(e.args[0], status.HTTP_400_BAD_REQUEST)






# @api_view(['POST'])
# def calcoulator(request):
#     try:
#         data=request.data

#     except:
#         pass


