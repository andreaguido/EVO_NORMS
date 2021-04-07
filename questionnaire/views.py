from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import datetime


class MyPage(Page):
	form_model = models.Player
	form_fields = ["age", "gender", "student", "discipline", "left_right", "experience"]
	timer_text = 'Tiempo restante para completar sus decisiones:'

	def set_extra_attributes(self):
		self.timeout_seconds = (self.session.config['start_datetime'] + datetime.timedelta(seconds=self.session.config['seconds_per_round']*(self.round_number+1)) - datetime.datetime.utcnow()).total_seconds()

#	def get_timeout_seconds(self):
#		return (self.participant.vars['expiry'] - datetime.datetime.utcnow()).total_seconds()

	def vars_for_template(self):
		return {
			'email': self.session.config['email'],
		}

	def before_next_page(self):
		if self.timeout_happened:
			self.player.timeout_MyPage = 1


class ResultsWaitPage(WaitPage):

	def after_all_players_arrive(self):
		pass


class Results(Page):
	pass


page_sequence = [
	MyPage,
]
