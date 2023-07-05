from django.urls import path
from . import views

urlpatterns = [
    path('planner/', views.planner, name='planner'),
    path('planner/chat', views.planner_chat, name='planner_chat'),
]