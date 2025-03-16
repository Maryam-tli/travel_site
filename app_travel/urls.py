from django.urls import path
from app_travel.views import *

urlpatterns = [
    path('', index_view, name="index"),
    path('home/', home_view, name="home"),
    path('about/', about_view, name="about"),
]