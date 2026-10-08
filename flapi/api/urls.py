from django.urls import path
from . import views

urlpatterns = [
    path('', views.getLeaderboard),
    path('leaderboard/', views.getLeaderboard),
    path('score/', views.submitScore)
]
