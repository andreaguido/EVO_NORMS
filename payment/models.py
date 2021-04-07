from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, BaseLink,
	Currency as c, currency_range
)

import random
import datetime

author = 'Aron Szekely'

doc = """
Payment screen for Climate Change Experiment
When the subject has been excluded payoff is set to 0 automatically
"""


class Constants(BaseConstants):
	name_in_url = 'page_pa'
	players_per_group = None
	num_rounds = 1
	timer_text = ''
	text_Inactive = 'payment/text_Inactive.html'
	endowment = c(30)

class Subsession(BaseSubsession):
	pass


class Group(BaseGroup):
	
	def set_payoffs(self):
		global winners
		active_players = [p for p in self.subsession.get_players() if p.inactive < self.session.config['inactive_threshold']]

		if len(active_players) > 0 and len(active_players) >= self.session.config['num_subjects_win']:
			winners = random.sample(active_players, self.session.config['num_subjects_win'])
		if len(active_players) > 0 and len(active_players) < self.session.config['num_subjects_win']:
			winners = random.sample(active_players, len(active_players))

		for p in self.get_players():
			# payoff from SVO
			p.slider_paid = p.participant.vars['slider_paid']
			p.self_paid = p.participant.vars['self_paid']
			p.payoff_svo = p.participant.vars['payoff_svo']

			# payoff from Norm Compliance
			p.payoff_norm_compliance = p.participant.vars['payoffNormCompliance']
			p.missed_decisions_norm_compliance = p.participant.vars['normcompliancemisseddecisions']

			# payoff from Lottery
			p.lottery_choice = p.participant.vars['lottery_choice'] + 1
			p.lottery_win = p.participant.vars['lottery_win']
			p.risk_lottery_payoff = p.participant.vars['risk_lottery_payoff']

			# payoffs from CPR game
			p.paying_round_week1 = p.participant.vars['paying_round_week1']
			p.paying_round_week2 = p.participant.vars['paying_round_week2']
			p.paying_round_week3 = p.participant.vars['paying_round_week3']
			p.paying_round_week4 = p.participant.vars['paying_round_week4']
			p.paying_round_week5 = p.participant.vars['paying_round_week5']

			p.expectations_payoff_week1 = p.participant.vars['expectations_payoff_week1']
			p.expectations_payoff_week2 = p.participant.vars['expectations_payoff_week2']
			p.expectations_payoff_week3 = p.participant.vars['expectations_payoff_week3']
			p.expectations_payoff_week4 = p.participant.vars['expectations_payoff_week4']
			p.expectations_payoff_week5 = p.participant.vars['expectations_payoff_week5']

			p.contribution_payoff_week1 = p.participant.vars['contribution_payoff_week1']
			p.contribution_payoff_week2 = p.participant.vars['contribution_payoff_week2']
			p.contribution_payoff_week3 = p.participant.vars['contribution_payoff_week3']
			p.contribution_payoff_week4 = p.participant.vars['contribution_payoff_week4']
			p.contribution_payoff_week5 = p.participant.vars['contribution_payoff_week5']

			if len(active_players) > 0:
				if p in winners:
					p.winner = 1
					win_week = random.sample([1, 2, 3, 4, 5], 1)

					if win_week[0] == 1:
						p.contribution_payoff_week1 = p.contribution_payoff_week1 * self.session.config['win_multiplier']
						p.win_week_var = 1
					elif win_week[0] == 2:
						p.contribution_payoff_week2 = p.contribution_payoff_week2 * self.session.config['win_multiplier']
						p.win_week_var = 2
					elif win_week[0] == 3:
						p.contribution_payoff_week3 = p.contribution_payoff_week3 * self.session.config['win_multiplier']
						p.win_week_var = 3
					elif win_week[0] == 4:
						p.contribution_payoff_week4 = p.contribution_payoff_week4 * self.session.config['win_multiplier']
						p.win_week_var = 4
					elif win_week[0] == 5:
						p.contribution_payoff_week5 = p.contribution_payoff_week5 * self.session.config['win_multiplier']
						p.win_week_var = 5

			# total payoff from CPR game
			p.game_total_payoff = p.contribution_payoff_week1 + p.contribution_payoff_week2 + p.contribution_payoff_week3 + p.contribution_payoff_week4 + p.contribution_payoff_week5 + p.expectations_payoff_week1 + p.expectations_payoff_week2 + p.expectations_payoff_week3 + p.expectations_payoff_week4 + p.expectations_payoff_week5

			# payoff from stage 7: punishment
			p.punishment_payoff = p.participant.vars['payoff_pun_prefs']

			if p.inactive >= self.session.config['inactive_threshold']:
				p.payoff = 0
			else:
				p.payoff = p.payoff_svo + p.risk_lottery_payoff + p.payoff_norm_compliance +\
						   p.game_total_payoff + p.punishment_payoff
				p.payoff_euros = round(p.payoff/30, 0)

class Player(BasePlayer):
	inactive = models.PositiveIntegerField()

	winner = models.IntegerField(default=0)  # player who won the lottery
	win_week_var = models.IntegerField(default=0)  # which week was chosen for the lottery

	slider_paid = models.PositiveIntegerField()
	self_paid = models.PositiveIntegerField()
	payoff_svo = models.CurrencyField()

	lottery_choice = models.PositiveIntegerField()
	lottery_win = models.PositiveIntegerField()
	risk_lottery_payoff = models.CurrencyField()

	paying_round_week1 = models.PositiveIntegerField()
	paying_round_week2 = models.PositiveIntegerField()
	paying_round_week3 = models.PositiveIntegerField()
	paying_round_week4 = models.PositiveIntegerField()
	paying_round_week5 = models.PositiveIntegerField()

	expectations_payoff_week1 = models.CurrencyField()
	expectations_payoff_week2 = models.CurrencyField()
	expectations_payoff_week3 = models.CurrencyField()
	expectations_payoff_week4 = models.CurrencyField()
	expectations_payoff_week5 = models.CurrencyField()

	contribution_payoff_week1 = models.CurrencyField()
	contribution_payoff_week2 = models.CurrencyField()
	contribution_payoff_week3 = models.CurrencyField()
	contribution_payoff_week4 = models.CurrencyField()
	contribution_payoff_week5 = models.CurrencyField()

	payoff_norm_compliance = models.CurrencyField()
	missed_decisions_norm_compliance = models.IntegerField()

	game_total_payoff = models.CurrencyField()

	punishment_payoff = models.CurrencyField()
	other_contribution = models.CurrencyField()
	belief_payoff = models.CurrencyField()
	timeout_MyPage1 = models.PositiveIntegerField()
	timeout_MyPage2 = models.PositiveIntegerField()

	payoff_euros = models.IntegerField()


class Link(BaseLink):
	pass