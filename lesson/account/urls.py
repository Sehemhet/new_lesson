from django.urls import path
from .views import *

urlpatterns = [
    path('', UsersDef, name='user_profile'),
]