from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants

import random

class PlayerBot(Bot):

	def play_round(self):
		if self.subsession.round_number==1:
			yield (views.Info)
		yield (views.Questions, {'selectionYellow': 1, 'selectionBlue': ""})
