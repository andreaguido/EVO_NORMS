from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants
from otree.api import Submission


class PlayerBot(Bot):

	def play_round(self):
		yield Submission(views.Initialisation, check_html=False)
		yield (views.Results, {'email_paypal':"SUCA"})

