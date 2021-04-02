from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import datetime

# to do:

class Initialisation(Page):
	timeout_seconds = 1

	def before_next_page(self):
		self.player.inactive = self.participant.vars['inactive']
		self.player.creating_score()
		self.participant.vars['score'] = self.player.score


class ShuffleWaitPage(WaitPage):
	wait_for_all_groups = True

	def after_all_players_arrive(self):
		sorted_players = sorted(
			self.subsession.get_players(),
			key=lambda player: player.participant.vars['score']
		)
		group_matrix = []
		ppg = Constants.players_per_group
		for i in range(0, len(sorted_players), ppg):
			group_matrix.append(sorted_players[i:i+ppg])
		self.subsession.set_group_matrix(group_matrix)


class PreviousResults(Page):
	timer_text = 'Time left to complete your decisions:'
	def get_timeout_seconds(self):
		self.participant.vars['expiry'] = self.session.config['start_datetime'] + datetime.timedelta(seconds=self.session.config['seconds_per_round']*(self.participant.vars['num_rounds']+2))
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
			'endowment': self.participant.vars['endowment'],
			'num_subjects_win': self.session.config['num_subjects_win'],
			'win_multiplier': self.session.config['win_multiplier'],
			'rounds': self.participant.vars['num_rounds']
			}


class MyPage1(Page):
	form_model = models.Player
	form_fields = ['decision_0', 'decision_1_5', 'decision_6_10', 'decision_11_15', 'decision_16_20', 'decision_21_25', 'decision_26_30']
	timer_text = 'Time left to complete your decisions:'

	def get_timeout_seconds(self):
		return (self.participant.vars['expiry'] - datetime.datetime.utcnow()).total_seconds()

	def vars_for_template(self):
		return {
			'inactive_threshold': self.session.config['inactive_threshold'],
			'email': self.session.config['email'],
		}

	def before_next_page(self):
		if self.timeout_happened:
			self.player.decision_0 = 0
			self.player.decision_1_5 = 0
			self.player.decision_6_10 = 0
			self.player.decision_11_15 = 0
			self.player.decision_16_20 = 0
			self.player.decision_21_25 = 0
			self.player.decision_26_30 = 0
			self.player.timeout_MyPage1 = 1
			self.player.inactive = self.player.inactive + 1

## remove ##
class MyPage2(Page):
	form_model = models.Player
	form_fields = ['others_decision_less_50', 'others_decision_50', 'others_decision_more_50']
	timer_text = 'Time left to complete your decisions:'

	def get_timeout_seconds(self):
		return (self.participant.vars['expiry'] - datetime.datetime.utcnow()).total_seconds()

	def vars_for_template(self):
		return {
			'inactive_threshold': self.session.config['inactive_threshold'],
			'email': self.session.config['email'],
		}

	def before_next_page(self):
		if self.timeout_happened:
			self.player.others_decision_less_50 = 0
			self.player.others_decision_50 = 0
			self.player.others_decision_more_50 = 0
			self.player.inactive = self.player.inactive + 1
			self.player.timeout_MyPage2 = 1
##

class WaitNextRound(Page):
	timer_text = 'Thank you for making your decisions. You will be shown your earnings in:'

	def get_timeout_seconds(self):
		return (self.participant.vars['expiry'] - datetime.datetime.utcnow()).total_seconds()

	def vars_for_template(self):
		return {
			'inactive_threshold': self.session.config['inactive_threshold'],
			'email': self.session.config['email'],
		}


class ResultsWaitPage1(WaitPage):
	wait_for_all_groups = True


class AnotherInitialisation(Page):
	timeout_seconds = 1
	
	def before_next_page(self):
		self.participant.vars['inactive'] = self.player.inactive
		self.player.calculate_belief_payoff()


class ResultsWaitPage2(WaitPage):

	def after_all_players_arrive(self):
		self.group.set_payoffs()


page_sequence = [
	Initialisation,
	ShuffleWaitPage,
	PreviousResults,
	MyPage1,
	#MyPage2,
	WaitNextRound,
	ResultsWaitPage1,
	#AnotherInitialisation,
	ResultsWaitPage2,
]