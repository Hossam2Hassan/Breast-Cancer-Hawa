from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, DjangoUnicodeDecodeError,force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.forms import ValidationError
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from .utils import Util


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    birthdate=serializers.DateField(required=True)
    first_name = serializers.CharField(max_length=100,required=True)
    last_name = serializers.CharField(max_length=100,required=True)
    phone=serializers.CharField(max_length=100,required=True)
    default_error_messages = {'status' : False,'username': 'The username should only contain alphanumeric characters'}

    class Meta:
        model = User
        fields = ['email', 'password','first_name','last_name','birthdate','phone']
    def save(self, **kwargs):
        user= User(
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            birthdate=self.validated_data['birthdate'],
            email=self.validated_data['email'],
            phone=self.validated_data['phone']
        )
        
        
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'status' : False,'message' : 'email is already exist', })

        
        if User.objects.filter(phone=self.validated_data['phone']).exists():
            raise serializers.ValidationError({'status' : False,'message' : 'phone is already exist', })

        user.set_password(self.validated_data['password'])
        user.save()
        return user

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    phone = serializers.CharField(max_length=11, min_length=3, read_only=True)
    first_name = serializers.CharField(max_length=255, min_length=3, read_only=True)

    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = User
        fields = ['first_name','email', 'password','phone', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
       
        filtered_user_by_email = User.objects.filter(email=email)
        user = auth.authenticate(email=email , password=password)

        if filtered_user_by_email.exists() and filtered_user_by_email[0].auth_provider != 'email':
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)

        if not user:
            raise AuthenticationFailed({'status':False,"messege":'Invalid Email or password, Try again'})
        if not user.is_active:
            raise AuthenticationFailed({'status':False,"messege":'Account not active, contact admin'})
        if not user.is_verified:
            raise AuthenticationFailed({'status':False,"messege":'Email is not Verified'})

        return{
            'email': user.email,
            'first_name':user.first_name,
            'phone':user.phone,
            'tokens': user.tokens
        }

        # return super().validate(attrs)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','birthdate','phone','age']


class PasswordChangeSerializer(serializers.Serializer): 
    oldpassword = serializers.CharField(max_length=68, min_length=6, write_only=True)
    new_password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    new_password_conf = serializers.CharField(max_length=68, min_length=6, write_only=True)




class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    error_message = {
        'bad_token': 'Token is expired or invalid'
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
           return Response( {'meassege':'bad_token'})

class PasswordforgetSerializer(serializers.Serializer):
  password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  password2 = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  class Meta:
    fields = ['password', 'password2']

  def validate(self, attr):
    try:
        password = attr.get('password')
        password2 = attr.get('password2')
        uid = self.context.get('uid')
        token = self.context.get('token')
        if password != password2:
            raise serializers.ValidationError("your Password doesn't match")
        id = smart_str(urlsafe_base64_decode(uid))
        user = User.objects.get(id=id)
        if not PasswordResetTokenGenerator().check_token(user, token):
            raise serializers.ValidationError('this Token is not Valid or Expired')
        user.set_password(password)
        user.save()
        return attr
    except DjangoUnicodeDecodeError as identifier:
        PasswordResetTokenGenerator().check_token(user, token)
        raise serializers.ValidationError('Token is not Valid or Expired')

class SendingSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=300)
    class Meta:
        fields=['email']
    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            request = self.context['request']
            site = get_current_site(request).domain
            link = 'http://'+site+'/auth/reset/'+ uid + '/'+token+ '/'
            body = 'Hi Desr,\nClick Following Link to Reset Your Password Please.\n'+link
            data = {
                'email_subject':'Reset Password',
                'email_body':body,
                'to_email':user.email
            }
            Util.send_email(data)
            return attrs
        else :
            raise serializers.ValidationError(
                {'status' : False,
                'message' :'Email incorrect'
            })

    
