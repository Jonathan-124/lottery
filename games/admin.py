from django.contrib import admin
from .models import Game


class GameAdmin(admin.ModelAdmin):
    model = Game
    readonly_fields = ('id',)


admin.site.register(Game, GameAdmin)
