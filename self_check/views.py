from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import  IsAuthenticated
from . import models
from rest_framework import generics
from rest_framework.response import Response
from .serializers import Self_checkSerializer,AnswerSerializer,CalenderSerializer
from rest_framework import status
# Create your views here.
from datetime import timedelta,datetime



# examination
@permission_classes(IsAuthenticated, )
@api_view(['GET','POST'])
def questionview(request):
    if request.method=='GET':
        data = {'question':[]}
        questions=models.Self_checkModel.objects.all()
        serializer=Self_checkSerializer(questions,many=True)
        for item in serializer.data:
            item['answer']= 'Yes / No'
            data['question'].append(item)
        return Response({'status':True,'data':data},status=status.HTTP_200_OK)



    elif request.method=='POST':
        try:
            question = models.Self_checkModel.objects.get(pk=request.data['self_check'])
            c= models.CheckingModel.objects.create(user=request.user , self_check=question, answer=request.data['answer'])
            return Response({'status':True, 'data':'data' },status=status.HTTP_200_OK)
        except:
            return Response({'status':True,'Error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
    


# request token response user self check question : answer 
@permission_classes(IsAuthenticated, )
@api_view(["GET"])
def reportview(request):
    if request.method=='GET':
        questions=models.CheckingModel.objects.all().filter(user=request.user)
        serializer=AnswerSerializer(questions,many=True)
        return Response({'status':True,'questions':serializer.data},status=status.HTTP_200_OK)


# request period date to return check dates
class Calender(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class=CalenderSerializer
    def post(self,request):
        serializer= self.serializer_class(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(self_check=request.user)
        date = datetime.strptime(request.data.get('period'),"%Y-%m-%d").date()
        checkList={"dates":[]}
        for i in range(7,11):
            checkdate = date + timedelta(days=i)
            b = {'date':checkdate}
            checkList['dates'].append(b)

        return Response({'status':True,'period date':date,'check_dates':checkList},status=status.HTTP_200_OK)

    def get(self,request):
        
        try:
            lastdate=models.CalendarModel.objects.filter(self_check=self.request.user).last()
            print(lastdate.period)
            checkList={"dates":[]}
            for i in range(7,11):
                checkdate = lastdate.period + timedelta(days=i)
                b = {'date':checkdate}
                checkList['dates'].append(b)
            return Response({'status':True,'period':lastdate.period,'data':checkList},status=status.HTTP_200_OK)
        except:
            return Response({'status':False,'meassage':'please enter period date '},status=status.HTTP_400_BAD_REQUEST)
        