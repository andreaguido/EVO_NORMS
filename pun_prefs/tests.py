from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants
from otree.api import Submission
import random


class PlayerBot(Bot):

	def play_round(self):
		yield Submission(views.Initialisation, timeout_happened=True, check_html=False)
		yield Submission(views.PreviousResults, timeout_happened=True, check_html=False)

		if self.player.inactive < self.session.config['inactive_threshold']:
			yield (views.MyPage1, {
				'decision_0': random.randint(0, Constants.endowment/3),
				'decision_1_5': random.randint(0, Constants.endowment/3),
				'decision_6_10': random.randint(0, Constants.endowment/3),
				'decision_11_15': random.randint(0, Constants.endowment/3),
				'decision_16_20': random.randint(0, Constants.endowment/3),
				'decision_21_25': random.randint(0, Constants.endowment/3),
				'decision_26_30': random.randint(0, Constants.endowment/3),
				})
			yield Submission(views.WaitNextRound, timeout_happened=True, check_html=False)

		elif self.player.inactive >= self.session.config['inactive_threshold']:
			yield Submission(views.MyPage1, timeout_happened=True, check_html=False)
			yield Submission(views.WaitNextRound, timeout_happened=True, check_html=False)
