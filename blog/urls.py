from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/<int:pk>', about, name='about')
]