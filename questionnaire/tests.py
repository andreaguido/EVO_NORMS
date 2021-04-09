from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants
from otree.api import Submission


class PlayerBot(Bot):
	# AND
	def play_round(self):
		yield Submission(views.MyPage,
						 {'age': 50,
						  'gender': 2,
						  'student': 1,
						  'discipline':"TEST",
						  'left_right':3,
						  'experience':0})
		
#		if self.player.inactive < self.session.config['inactive_threshold']:
#			yield (views.MyPage, {'feedback': "blah"})
#		elif self.player.inactive >= self.session.config['inactive_threshold']:
#			yield Submission(views.MyPage, timeout_happened=True, check_html=False)