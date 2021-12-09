from django.urls import path 
from appOne import views

urlpatterns = [
    path('', views.projectpage.as_view())
]


