from django.urls import path
from .views import RegisterView, LogoutAPIView,SendingEmail, PasswordforgetView,GetUpdateProfile,PasswordChange, VerifyEmail, LoginAPIView
from rest_framework_simplejwt.views import (TokenRefreshView,)
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('register/', RegisterView.as_view(), name="register"),
     path('login/', LoginAPIView.as_view(), name="login"),
     path('logout/', LogoutAPIView.as_view(), name="logout"),
     path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path('password/change/', PasswordChange.as_view(),name='authemail-password-change'),

     path('sending/', SendingEmail.as_view(), name= 'reset'),
     path('forgetpassword/<uid>/<token>/', PasswordforgetView.as_view()),

     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name= 'password_reset_confirm'),
     path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name= 'password_reset_complete'),

     path('profile/' ,GetUpdateProfile.as_view(), name = 'profile'),
     
]
