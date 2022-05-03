from django.urls import path
from . import views 
urlpatterns = [
    path('questians/',views.questionview,name='ques'),
    path('report/',views.reportview,name='report'),
    path('calender/',views.Calender.as_view(),name='calender'),
]