

from django.urls import path
from fadir.views import funcLogin, pagHome




urlpatterns = [
  
    path('login/', funcLogin),
    path('', pagHome),
]
