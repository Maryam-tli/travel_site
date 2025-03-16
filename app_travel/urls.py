from django.urls import path
from app_travel.views import *

urlpatterns = [
    path('', index_view, name="index"),
]