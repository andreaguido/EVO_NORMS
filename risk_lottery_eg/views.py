from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import datetime


class MyPage(Page):
	form_model = models.Player
	form_fields = ['choice']
	#timer_text = 'Time left to complete your decisions:'

	def get_timeout_seconds(self):
		return (self.participant.vars['expiry'] - datetime.datetime.utcnow()).total_seconds()

	def vars_for_template(self):
		return {'email': self.session.config['email']}

	def before_next_page(self):
		self.player.calc_pay()

		if self.timeout_happened:
			self.player.timeout_MyPage = 1


class ResultsWaitPage(WaitPage):

	def after_all_players_arrive(self):
		pass


class Results(Page):
	pass


page_sequence = [
	MyPage,
	#ResultsWaitPage,
	#Results
]
