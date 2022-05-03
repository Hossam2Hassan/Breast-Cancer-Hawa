from django.urls import path
from . import views

urlpatterns = [
    path('11/', views.prediction11,name='prediction'),
    path('',views.PredictionkView.as_view(),name='prediction0')
]
