from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import datetime


class MyPage(Page):
	form_model = models.Player
	form_fields = ["age", "gender", "student", "discipline", "left_right", "experience"]
	timer_text = 'Time left respond:'

	def get_timeout_seconds(self):
		return (self.participant.vars['expiry'] - datetime.datetime.utcnow()).total_seconds()

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
