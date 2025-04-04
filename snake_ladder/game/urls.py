from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_view, name='start_view'),
    path('game/', views.game_view, name='game_view'),
    path('new/', views.new_game, name='new_game'),
]