from django.urls import path

from .views import HomePageView 
from . import views

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('', HomePageView.as_view(), name='home'), 
]
    