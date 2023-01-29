from django.urls import path

from .views import HomePageView 
from . import views

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('', HomePageView.as_view(), name='home'),
    path('portfolio/', views.portfolio_view, name='portfolio_view'),
    path('trade/', views.trade_view, name='trade_view'), 
    path('success/<str:crypto>', views.success_view, name='success_view'), 
]
    