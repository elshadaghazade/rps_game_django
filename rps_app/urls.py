from django.urls import path
from .views import *

urlpatterns = [
    path('', authenticate, name='authentication'),
    path('play/', play, name='play'),
    path('logout/', logout, name='logout'),
    path('statistics/', statistics, name='statistics')
]
