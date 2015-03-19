from django.contrib import admin
from ranks.models import Series, Player, Game

class GameInline(admin.TabularInline):
	model = Game
	extra = 0

class PlayerInline(admin.TabularInline):
	model = Player
	extra = 0

class SeriesAdmin(admin.ModelAdmin):
	inlines = [PlayerInline, GameInline]

admin.site.register(Series, SeriesAdmin)