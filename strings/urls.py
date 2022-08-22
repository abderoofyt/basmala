from django.urls import path
from . import views

urlpatterns = [
    path('', views.strings, name='strings'),
    path('hello/', views.hello, name='hello'),
    path('home/', views.home, name='home'),
    path('context/', views.context, name='context'),
    path('bismala/', views.bismala, name='bismala'),
]