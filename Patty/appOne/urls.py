from django.urls import path 
from appOne import views

urlpatterns = [
    path('', views.pattyprojectpage.asview(), name ='home')
]