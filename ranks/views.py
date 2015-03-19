from django.shortcuts import render
from ranks.models import Series, Player, Game
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone

def index(request):
	series = Series.objects.get(pk=1)
	players = series.player_set.order_by('rank')

	context = {'players': players, 'series': series}
	return render(request, 'ranks/index.html', context)

def add_player_detail(request):
	series = Series.objects.get(pk=1)

	context = {'series': series}
	return render(request, 'ranks/add-player-form.html', context)

def add_player(request):
	series = Series.objects.get(pk=1)

	first_name_input = request.POST['firstname']
	last_name_input = request.POST['lastname']

	new_player = Player(
			first_name=first_name_input,
			last_name=last_name_input,
			series=series,
		)
	new_player.save()

	series.update_rankings()

	return HttpResponseRedirect(reverse('ranks:index'))

def add_game_detail(request):
	series = Series.objects.get(pk=1)
	players = series.player_set.all()

	context = {'players': players, 'series': series}
	return render(request, 'ranks/add-game-detail.html', context)

def add_game_places(request):
	series = Series.objects.get(pk=1)

	buy_in = float(request.POST['buyin'].lstrip('$'))

	first_place_amount = float(request.POST['firstplace'].lstrip('$'))
	second_place_amount = float(request.POST['secondplace'].lstrip('$'))
	third_place_amount = float(request.POST['thirdplace'].lstrip('$'))
	fourth_place_amount = float(request.POST['fourthplace'].lstrip('$'))

	new_game = Game(
			buy_in_amount=buy_in,
			first_earnings=first_place_amount,
			second_earnings=second_place_amount,
			third_earnings=third_place_amount,
			fourth_earnings=fourth_place_amount,
			date_played=timezone.now(),
			series=series,
		)
	new_game.save()

	game_id = new_game.id

	players = []
	for idValue in request.POST.getlist('players[]'):
		players.append(series.player_set.get(pk=idValue))

	for player in players:
		player.subtract_buy_in(buy_in)
		player.increment_games_played_count()
		player.games_played_in.add(new_game)
		player.save()

	context = {'players': players, 'series': series, 'game_id': game_id}
	return render(request, 'ranks/add-game-places.html', context)

def add_game(request, game_id):
	series = Series.objects.get(pk=1)
	game = series.game_set.get(pk=game_id)

	for idValue in request.POST.getlist('buyin[]'):
		player = series.player_set.get(pk=idValue)
		player.subtract_buy_in(game.buy_in_amount)
		player.save()
		game.update_first_earnings()

	first_place_player = series.player_set.get(pk=request.POST['firstplace'])
	second_place_player = series.player_set.get(pk=request.POST['secondplace'])
	third_place_player = series.player_set.get(pk=request.POST['thirdplace'])
	fourth_place_player = series.player_set.get(pk=request.POST['fourthplace'])

	first_place_player.increment_first_places_count()
	first_place_player.update_earnings(game.first_earnings)
	first_place_player.save()

	second_place_player.increment_second_places_count()
	second_place_player.update_earnings(game.second_earnings)
	second_place_player.save()

	third_place_player.increment_third_places_count()
	third_place_player.update_earnings(game.third_earnings)
	third_place_player.save()

	fourth_place_player.increment_fourth_places_count()
	fourth_place_player.update_earnings(game.fourth_earnings)
	fourth_place_player.save()

	game.update_first_id(first_place_player.id)
	game.update_second_id(second_place_player.id)
	game.update_third_id(third_place_player.id)
	game.update_fourth_id(fourth_place_player.id)
	game.save()

	series.update_rankings()

	return HttpResponseRedirect(reverse('ranks:index'))