from django.urls import path
from .views import GameView, MethodologyView, SitemapView


urlpatterns = [
    path('', GameView.as_view(), {'pk': 1}, name='game_view'),
    path('methodology/', MethodologyView.as_view(), {'pk': 1}, name='methodology_view'),
    path('sitemap.xml/', SitemapView.as_view(), name='sitemap_view'),
]
