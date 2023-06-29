from django.urls import path
from companies import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<uuid:pk>', views.get_company, name='get_company'),
]
