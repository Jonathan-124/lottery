from django.urls import path
from .views import GameView, MethodologyView


urlpatterns = [
    path('', GameView.as_view(), {'pk': 1}, name='game_view'),
    path('methodology/', MethodologyView.as_view(), {'pk': 1}, name='methodology_view'),
]
