from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.hello, name='hello'),

    path('home/', views.home),

    path('context/', views.context),

    path('bismal/', views.bismala, name='bismala'),
]