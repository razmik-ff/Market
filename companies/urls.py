from django.urls import path
from companies import views

urlpatterns = [
    path('', views.home, name='home')
]
