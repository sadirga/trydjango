from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hei/', views.hey)
]