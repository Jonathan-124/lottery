from django.contrib import admin
from .models import Draw


class DrawAdmin(admin.ModelAdmin):
    model = Draw


admin.site.register(Draw, DrawAdmin)
