from django.urls import path
from . import views

urlpatterns = [
    path('', views.RiskView.as_view(),name='risk')
]
