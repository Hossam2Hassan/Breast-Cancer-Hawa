from django.shortcuts import render
from rest_framework import generics, status, views, permissions
from .serializers import (RegisterSerializer, LogoutSerializer,UserSerializer,SendingSerializer,PasswordforgetSerializer, EmailVerificationSerializer, LoginSerializer, PasswordChangeSerializer)
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework.permissions import AllowAny, IsAuthenticated
import jwt
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .renderers import UserRenderer
from django.contrib.sites.shortcuts import get_current_site
from .utils import Util
from django.http import HttpResponsePermanentRedirect
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken

from rest_framework.views import APIView


class RegisterView(generics.GenericAPIView):
    authentication_classes=()
    serializer_class = RegisterSerializer
    # renderer_classes = (UserRenderer,)

    def post(self, request):
        user0 = request.data
        serializer = self.serializer_class(data=user0)
        serializer.is_valid()
        
        if User.objects.filter(email=user0['email']).exists():
            return Response({'status' : False,'message' : 'هذا البريد موجود بالفعل', })

        
        if User.objects.filter(phone=user0['phone']).exists():
            return Response({'status' : False,'message' : 'رقم الهاتف مسجل مسبقا', })
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user0['email'])
        token = RefreshToken.for_user(user).access_token
        # token = PasswordResetTokenGenerator().make_token(user)
        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')
        absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
        email_body = 'Hi '+user.first_name + \
            ' Use the link below to verify your email \n' + absurl
        print(str(token))
        data = {'email_body': email_body, 'to_email': user.email,
                'email_subject': 'Verify email'}

        Util.send_email(data)
        return Response({'status':True ,
        'message':'تم ارسال رابط الي البريد الخاص بك',
        'user_data':user_data}, status=status.HTTP_201_CREATED)


class VerifyEmail(views.APIView):
    authentication_classes=()
    serializer_class = EmailVerificationSerializer

    token_param_config = openapi.Parameter(
        'token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])
            # payload = jwt.decode(token, settings.SECRET_KEY)
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            # return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
                return render (request,'activation_success.html')
            else:
                return render (request,'activated.html')
        except jwt.ExpiredSignatureError as identifier:
            # return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
            return render (request,'activation_expired.html')
        except jwt.exceptions.DecodeError as identifier:
            # return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
            return render (request,'activation_invalid.html')
from django.contrib import auth
class LoginAPIView(generics.GenericAPIView):
    authentication_classes={}
    serializer_class = LoginSerializer

    def post(self, request):
        user=request.data
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
       
            email = user.get('email')
            password = user.get('password')
            
            filtered_user_by_email = User.objects.filter(email=email)
            user = auth.authenticate(email=email , password=password)
            if not user:
                return Response({'status':False,"messege":'خطأ في البريد او الرقم السري',"user_data":{}}, status=status.HTTP_200_OK)
            if not user.is_active:
                return Response({'status':False,"messege":'الحساب متوقف من قبل الادمن',"user_data":{}}, status=status.HTTP_200_OK)
            if not user.is_verified:
                user=request.data
                user0 = User.objects.get(email=user['email'])
                token = RefreshToken.for_user(user0).access_token
                # token = PasswordResetTokenGenerator().make_token(user)
                current_site = get_current_site(request).domain
                relativeLink = reverse('email-verify')
                absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
                email_body = 'Hi '+user0.first_name + \
                    ' Use the link below to verify your email \n' + absurl
                print(str(token))
                data = {'email_body': email_body, 'to_email': user0.email,
                        'email_subject': 'Verify email'}

                Util.send_email(data)
                return Response({'status':False ,
                'messege':' هذا الحساب غير مفعل راجع البريد الخاص بك'})
                # return Response({'status':False,"messege":'الحساب غير مفعل',"user_data":{}}, status=status.HTTP_200_OK)
            if filtered_user_by_email.exists() and filtered_user_by_email[0].auth_provider != 'email':
               pass
            return Response({'status':True,"messege":"مرحباً..!","user_data":serializer.data}, status=status.HTTP_200_OK)
        return Response({'status':False,"messege":'..!خطأ في البريد او الرقم السري',"user_data":{}}, status=status.HTTP_400_BAD_REQUEST)

        




class PasswordChange(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PasswordChangeSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = request.user
            oldpassword=request.data['oldpassword']
            new_password = request.data['new_password']
            new_password_conf = request.data['new_password_conf']
            if  not user.check_password(oldpassword):
                return Response({'status':False,'messege':'old_password is not correct'})
            if new_password!=new_password_conf:
                return Response({'status':False,'messege':'password is not mached'})
            user.set_password(new_password)
            user.save()
            content = {'success': ('your Password changed successfully.')}
            return Response(content, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    serializer_class = LogoutSerializer

    permission_classes = (permissions.IsAuthenticated,)
    # def post(self, request, *args, **kwargs):
    #     if self.request.data.get('all'):
    #         token: OutstandingToken
    #         for token in OutstandingToken.objects.filter(user=request.user):
    #             _, _ = BlacklistedToken.objects.get_or_create(token=token)
    #             token.access_token.delete()
                
    #         return Response({"status": "OK, goodbye, all refresh tokens blacklisted"})
    #     refresh_token = self.request.data.get('refresh_token')
    #     token = RefreshToken(token=refresh_token)
    #     token.blacklist()
        
    #     return Response({"status": "OK, goodbye"})
    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'status':True,'message':'log out successfully'},status=status.HTTP_204_NO_CONTENT)

# profile of user GET to show user info and PUT to mdifay user info
class GetUpdateProfile(APIView):
    permission_classes = [permissions.IsAuthenticated,]
    def put(self,request, *args , **kwargs):
        try:
            user = self.request.user
            print(user)
        except User.DoesNotExist:
            return Response({ 'status' : False ,'message' :'Token invalid'},status=status.HTTP_404_NOT_FOUND)
        userSerializer = UserSerializer(user,data=request.data)
        if userSerializer.is_valid() :
            userSerializer.save()
            return Response({'status': True,'message' :'تم تعديل...!','data':[ userSerializer.data]} ,status=status.HTTP_202_ACCEPTED)
        else:
            return Response({ 'status' : False ,'message' :'Error data '},status=status.HTTP_404_NOT_FOUND)
    def get(self, request, format=None):
        try:
            user = self.request.user
            print(user)
        except User.DoesNotExist:
            return Response({ 'status' : False ,'message' :'Token invalid'},status=status.HTTP_404_NOT_FOUND)
        userSerializer = UserSerializer(user)
        return Response({'status': True,'data':[ userSerializer.data ]} ,status=status.HTTP_200_OK)



#request email address response send link to user email's 
class SendingEmail(generics.GenericAPIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = SendingSerializer
    def post(self,request,format=None):
        serializer = self.get_serializer(data =request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'status': True,'messege' : 'تم ارسال رابط الي البريد الخاص بك'},status=status.HTTP_200_OK)
        return Response({'status' : False,'messege': 'email'}, status=status.HTTP_401_UNAUTHORIZED)

    
# request uid - token fron url and password , repassword from user
class PasswordforgetView(APIView):
    def post(self, request, uid, token, format=None):
        serializer = PasswordforgetSerializer(data=request.data, context={'uid':uid, 'token':token})
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'your Password Reset Successfully'}, status=status.HTTP_200_OK)

class DeleteUserViews(APIView):
    
    def post(self, request):
        user=request.user
        try:
            if User.objects.filter(email=user.email).exists():
                user = User.objects.get(email=user.email)
                print(request.user)
                user.delete()
            return Response({"status":True,"Messege":"account deleted"})
        except:
            return Response({"status":False,"Messege":"account not found"})