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


class PreviousResults(Page):
	timer_text = Constants.timer_text

	def get_timeout_seconds(self):
		self.participant.vars['expiry'] = self.session.config['start_datetime'] + datetime.timedelta(
			seconds=self.session.config['seconds_per_round'] * (self.round_number + 1))
		return (self.participant.vars['expiry'] - datetime.datetime.utcnow()).total_seconds()

	def vars_for_template(self):
		return {
			'display_payoff': self.participant.vars['unconditional_payoff'],
			'inactive_threshold': self.session.config['inactive_threshold'],
			'previous_round_number': self.participant.vars['previous_round_number'],
			'previous_contribution': self.participant.vars['contribution'],
			'previous_total_contribution': self.participant.vars['total_contribution'],
			'previous_unconditional_payoff': self.participant.vars['unconditional_payoff'],
			'previous_other_contribution0': self.participant.vars['other_contribution0'],
			'previous_other_contribution1': self.participant.vars['other_contribution1'],
			'previous_other_contribution2': self.participant.vars['other_contribution2'],
			'previous_other_contribution3': self.participant.vars['other_contribution3'],
			'previous_other_contribution4': self.participant.vars['other_contribution4'],
			'previous_other_inactive0': self.participant.vars['other_inactive0'],
			'previous_other_inactive1': self.participant.vars['other_inactive1'],
			'previous_other_inactive2': self.participant.vars['other_inactive2'],
			'previous_other_inactive3': self.participant.vars['other_inactive3'],
			'previous_other_inactive4': self.participant.vars['other_inactive4'],
			'previous_other_timeout_Contribute0': self.participant.vars['other_timeout_Contribute0'],
			'previous_other_timeout_Contribute1': self.participant.vars['other_timeout_Contribute1'],
			'previous_other_timeout_Contribute2': self.participant.vars['other_timeout_Contribute2'],
			'previous_other_timeout_Contribute3': self.participant.vars['other_timeout_Contribute3'],
			'previous_other_timeout_Contribute4': self.participant.vars['other_timeout_Contribute4'],
			'email': self.session.config['email'],
			'num_subjects_win': self.session.config['num_subjects_win'],
			'win_multiplier': self.session.config['win_multiplier'],
			'rounds': self.round_number
		}

class Results(Page):
	timer_text = 'Time left to confirm your earnings:'

	def get_timeout_seconds(self):
		self.participant.vars['expiry'] = self.session.config['start_datetime'] + datetime.timedelta(seconds=self.session.config['seconds_per_round']*(self.participant.vars['num_rounds']+3))
		return (self.participant.vars['expiry'] - datetime.datetime.utcnow()).total_seconds()

	def vars_for_template(self):
		return {
			'inactive_threshold': self.session.config['inactive_threshold'],
			'email': self.session.config['email'],
			'num_subjects_win': self.session.config['num_subjects_win'],
			'win_multiplier': self.session.config['win_multiplier'],
		}


page_sequence = [
	Initialisation,
	#PreviousResults,
	ResultsWaitPage,
	Results
]
