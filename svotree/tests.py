from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants
from otree.api import Submission
import random


class PlayerBot(Bot):
	def play_round(self):
#		yield (views.SliderPrimaryContinuous, {
#			'slider1': 50,
#			'slider2': 50,
#			'slider3': 50,
#			'slider4': 50,
#			'slider5': 50,
#			'slider6': 50,
#			})
#		assert self.player.slider2_self == 92		#slight rounding issue: to be sorted out
#		assert self.player.slider2_other == 32
		yield (views.SliderPrimaryContinuous, {
				'slider1': random.randint(0, 100),
				'slider2': random.randint(0, 100),
				'slider3': random.randint(0, 100),
				'slider4': random.randint(0, 100),
				'slider5': random.randint(0, 100),
				'slider6': random.randint(0, 100),
				})

#		yield (views.SliderPrimaryContinuous, {
#			'slider1': 100,
#			'slider2': 100,
#			'slider3': 100,
#			'slider4': 100,
#			'slider5': 100,
#			'slider6': 100,
#			})
		
		yield Submission(views.WaitNextRound, check_html=False)