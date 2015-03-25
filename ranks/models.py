import datetime

from django.db import models
from django.utils import timezone

class Series(models.Model):
	name = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = 'series'

	def __str__(self):
		return self.name

	def update_rankings(self):
		players = self.player_set.order_by('-score')
		series_games_played = self.game_set.order_by('-id')[:10]

		series_games_ids = []
		for game in series_games_played:
			series_games_ids.append(game.id)

		points_possible = 4.0 * len(series_games_played)

		for player in players:
			points_earned = 0.0
			player_games_played = player.games_played_in.order_by('-id')[:10]
			for game in player_games_played:
				if game.id in series_games_ids:
					if game.first_id == player.id:
						points_earned += 4.0
					elif game.second_id == player.id:
						points_earned += 3.0
					elif game.third_id == player.id:
						points_earned += 2.0
					elif game.fourth_id == player.id:
						points_earned += 1.0
			try:			
				player.update_score(points_earned / points_possible)
			except:
				player.update_score(0.0)	
			player.save()

		players = self.player_set.order_by('-score')
		new_ranking = 1
		ranking_value = 1
		for index,player in enumerate(players):
			player.update_ranking(ranking_value)
			player.save()
			new_ranking += 1
			try:
				if player.score != players[index + 1].score:
					ranking_value = new_ranking
			except:
				break		

class Game(models.Model):
	first_id = models.IntegerField(default=-1)
	second_id = models.IntegerField(default=-1)
	third_id = models.IntegerField(default=-1)
	fourth_id = models.IntegerField(default=-1)

	buy_in_amount = models.FloatField(default=0.00)

	first_earnings = models.FloatField(default=0.00)
	second_earnings = models.FloatField(default=0.00)
	third_earnings = models.FloatField(default=0.00)
	fourth_earnings = models.FloatField(default=0.00)

	date_played = models.DateTimeField('Date Played')

	series = models.ForeignKey(Series)

	def __str__(self):
		return str(self.id)

	def update_first_earnings(self):
		self.first_earnings += self.buy_in_amount

	def update_first_id(self, new_id):
		self.first_id = new_id

	def update_second_id(self, new_id):
		self.second_id = new_id

	def update_third_id(self, new_id):
		self.third_id = new_id

	def update_fourth_id(self, new_id):
		self.fourth_id = new_id			

class Player(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)

	first_places = models.IntegerField(default=0)
	second_places = models.IntegerField(default=0)
	third_places = models.IntegerField(default=0)
	fourth_places = models.IntegerField(default=0)

	earnings = models.FloatField(default=0.00)

	games_played_in = models.ManyToManyField(Game)
	total_games_played = models.IntegerField(default=0)

	series = models.ForeignKey(Series)
	score = models.FloatField(default=0.0)
	rank = models.IntegerField(default=9999)

	def __str__(self):
		return self.first_name + ' ' + self.last_name

	def get_win_percentage(self):
		try:
			percentage = float(self.first_places) / float(self.total_games_played) * 100
			return '{:.2f}'.format(percentage)
		except:
			return str(0)

	def get_earnings(self):
		if self.earnings >= 0:
			return '$' + str('{:.2f}'.format(self.earnings))
		return '-$' + str('{:.2f}'.format(-1 * self.earnings))

	def get_first_initial(self):
		return self.first_name[0]

	def get_last_initial(self):
		return self.last_name[0]

	def update_score(self, new_score):
		self.score = new_score

	def update_ranking(self, new_ranking):
		self.rank = new_ranking

	def increment_games_played_count(self):
		self.total_games_played += 1

	def subtract_buy_in(self, buy_in_value):
		self.earnings -= buy_in_value

	def increment_first_places_count(self):
		self.first_places += 1

	def increment_second_places_count(self):
		self.second_places += 1

	def increment_third_places_count(self):
		self.third_places += 1		

	def increment_fourth_places_count(self):
		self.fourth_places += 1

	def update_earnings(self, new_earnings):
		self.earnings += new_earnings	