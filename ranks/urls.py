from django.conf.urls import patterns, url
from ranks import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^games$', views.game_viewer, name='game-viewer'),
	url(r'^add-player$', views.add_player_detail, name='add-player-detail'),
	url(r'^add-player-update$', views.add_player, name='add-player'),
	url(r'^add-game/gameid=(?P<game_id>[0-9A-Za-z._%+-]+)', views.add_game, name='add-game'),
	url(r'^add-game-cont', views.add_game_places, name='add-game-places'),
	url(r'^add-game', views.add_game_detail, name='add-game-detail'),
)