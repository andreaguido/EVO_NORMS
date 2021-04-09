from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import datetime


class Initialisation(Page):
	timeout_seconds = 1

	def before_next_page(self):
		self.player.inactive = self.participant.vars['inactive']

class ResultsWaitPage(WaitPage):

	def after_all_players_arrive(self):
		self.group.set_payoffs()

class Results(Page):
	timer_text = ''
	form_model = models.Player
	form_fields = ['email_paypal']

	def set_extra_attributes(self):
		self.timeout_seconds = (self.session.config['start_datetime'] + datetime.timedelta(seconds=self.session.config['seconds_per_round']*(self.participant.vars['num_rounds']+3)) - datetime.datetime.utcnow()).total_seconds()

#	def get_timeout_seconds(self):
#		self.participant.vars['expiry'] = self.session.config['start_datetime'] + datetime.timedelta(seconds=self.session.config['seconds_per_round']*(self.participant.vars['num_rounds']+3))
#		return (self.participant.vars['expiry'] - datetime.datetime.utcnow()).total_seconds()

	def vars_for_template(self):
		return {
			'inactive_threshold': self.session.config['inactive_threshold'],
			'email': self.session.config['email'],
			'num_subjects_win': self.session.config['num_subjects_win'],
			'win_multiplier': self.session.config['win_multiplier'],
			'rate': self.session.config['puntos_euro_rate']
		}


page_sequence = [
	Initialisation,
	ResultsWaitPage,
	Results
]
