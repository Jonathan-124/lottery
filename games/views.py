from django.views.generic import DetailView
from .models import Game


class GameView(DetailView):
    model = Game
    template_name = 'game.html'


class MethodologyView(DetailView):
    model = Game
    template_name = 'methodology.html'
