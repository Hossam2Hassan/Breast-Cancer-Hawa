from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken
import uuid

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password,**extra_fields):
        # if username is None:
        #     raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password,**extra_fields):
        if password is None:
            raise TypeError('Password should not be none')
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user



AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google','email': 'email'}

class User(AbstractBaseUser, PermissionsMixin):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True, db_index=True,blank=True,null=True)
    email = models.EmailField(max_length=200, unique=True, db_index=True)
    birthdate=models.DateField(null=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))
    phone= models.CharField(max_length=11 , null =True)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

