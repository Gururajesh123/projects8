from django.urls import path
from app2.views import *
app_name='night'

urlpatterns=[
    path('bye/',bye,name='bye'),
]