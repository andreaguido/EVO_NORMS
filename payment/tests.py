from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants
from otree.api import Submission


class PlayerBot(Bot):

	def play_round(self):
		yield Submission(views.Initialisation, timeout_happened=True, check_html=False)
		
		if self.player.inactive < self.session.config['inactive_threshold']:
			yield (views.Results)
		elif self.player.inactive >= self.session.config['inactive_threshold']:
			yield Submission(views.Results, timeout_happened=True, check_html=False)


