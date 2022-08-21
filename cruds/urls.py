from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_view),
    path('list/', views.list_view),
    path('list/<id>/', views.detail_view),
    path('list/<id>/update/', views.update_view),
    path('list/<id>/delete/', views.delete_view),

]