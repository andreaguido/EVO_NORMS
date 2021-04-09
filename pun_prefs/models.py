from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, BaseLink,
	Currency as c, currency_range
)

import random
from statistics import mean

author = 'Aron Szekely'

doc = """
Third-party punishment preference elicitation
"""


class Constants(BaseConstants):
	name_in_url = 'page_pu'
	players_per_group = 2
	other_players_per_group = 5

	num_rounds = 1
	endowment = 30
	cost_rate = 3

	text_Inactive = 'pun_prefs/text_Inactive.html'
	text_Instructions = 'pun_prefs/text_Instructions.html'


class Subsession(BaseSubsession):
	pass 


class Group(BaseGroup):

	# here define payoff from punishment stage
	def set_payoffs(self):
		p1 = self.get_player_by_id(1)
		p2 = self.get_player_by_id(2)

		p1.self_paid = random.randint(0, 1)  # define
		p1.other_contribution = p2.participant.vars['final_round_contribution']
		p2.other_contribution = p1.participant.vars['final_round_contribution']

		# check: this should be the payoff from belief on punishment (DELETE)
		#p1.belief_payoff = p1.others_decision_less_50_payoff + p1.others_decision_50_payoff + p1.others_decision_more_50_payoff
		#p2.belief_payoff = p2.others_decision_less_50_payoff + p2.others_decision_50_payoff + p2.others_decision_more_50_payoff

		if p1.self_paid == 1:
			p2.self_paid = 0
			if p1.other_contribution == 0:
				p1.payoff = Constants.endowment - p1.decision_0
				p2.payoff = Constants.endowment - p1.decision_0*3
				p1.punish = p1.decision_0
				p2.punish = p1.decision_0*3
			if 1 <= p1.other_contribution <= 5:
				p1.payoff = Constants.endowment - p1.decision_1_5
				p2.payoff = Constants.endowment - p1.decision_1_5*3
				p1.punish = p1.decision_1_5
				p2.punish = p1.decision_1_5*3
			if 6 <= p1.other_contribution <= 10:
				p1.payoff = Constants.endowment - p1.decision_6_10
				p2.payoff = Constants.endowment - p1.decision_6_10*3
				p1.punish = p1.decision_6_10
				p2.punish = p1.decision_6_10*3
			if 11 <= p1.other_contribution <= 15:
				p1.payoff = Constants.endowment - p1.decision_11_15
				p2.payoff = Constants.endowment - p1.decision_11_15*3
				p1.punish = p1.decision_11_15
				p2.punish = p1.decision_11_15*3
			if 16 <= p1.other_contribution <= 20:
				p1.payoff = Constants.endowment - p1.decision_16_20
				p2.payoff = Constants.endowment - p1.decision_16_20*3
				p1.punish = p1.decision_16_20
				p2.punish = p1.decision_16_20*3
			if 21 <= p1.other_contribution <= 25:
				p1.payoff = Constants.endowment - p1.decision_21_25
				p2.payoff = Constants.endowment - p1.decision_21_25*3
				p1.punish = p1.decision_21_25
				p2.punish = p1.decision_21_25*3
			if 26 <= p1.other_contribution <= 30:
				p1.payoff = Constants.endowment - p1.decision_26_30
				p2.payoff = Constants.endowment - p1.decision_26_30*3
				p1.punish = p1.decision_26_30
				p2.punish = p1.decision_26_30*3

		elif p1.self_paid == 0:
			p2.self_paid = 1
			if p2.other_contribution == 0:
				p2.payoff = Constants.endowment - p2.decision_0
				p1.payoff = Constants.endowment - p2.decision_0*3
				p2.punish = p2.decision_0
				p1.punish = p2.decision_0*3
			if 1 <= p2.other_contribution <= 5:
				p2.payoff = Constants.endowment - p2.decision_1_5
				p1.payoff = Constants.endowment - p2.decision_1_5*3
				p2.punish = p2.decision_1_5
				p1.punish = p2.decision_1_5*3
			if 6 <= p2.other_contribution <= 11:
				p2.payoff = Constants.endowment - p2.decision_6_10
				p1.payoff = Constants.endowment - p2.decision_6_10*3
				p2.punish = p2.decision_6_10
				p1.punish = p2.decision_6_10*3
			if 11 <= p1.other_contribution <= 15:
				p2.payoff = Constants.endowment - p2.decision_11_15
				p1.payoff = Constants.endowment - p2.decision_11_15*3
				p2.punish = p2.decision_11_15
				p1.punish = p2.decision_11_15*3
			if 16 <= p2.other_contribution <= 20:
				p2.payoff = Constants.endowment - p2.decision_16_20
				p1.payoff = Constants.endowment - p2.decision_16_20*3
				p2.punish = p2.decision_16_20
				p1.punish = p2.decision_16_20*3
			if 21 <= p2.other_contribution <= 25:
				p2.payoff = Constants.endowment - p2.decision_21_25
				p1.payoff = Constants.endowment - p2.decision_21_25*3
				p2.punish = p2.decision_21_25
				p1.punish = p2.decision_21_25*3
			if 26 <= p2.other_contribution <= 30:
				p2.payoff = Constants.endowment - p2.decision_26_30
				p1.payoff = Constants.endowment - p2.decision_26_30*3
				p2.punish = p2.decision_26_30
				p1.punish = p2.decision_26_30*3

		for p in self.get_players():
			if p.timeout_MyPage1 == 0:
				p.participant.vars['payoff_pun_prefs'] = p.payoff
			elif p.timeout_MyPage1 == 1:
				p.participant.vars['payoff_pun_prefs'] = 0
			#p.participant.vars['belief_payoff'] = p.belief_payoff
			p.participant.vars['pun_prefs_self_paid'] = p.self_paid
			p.participant.vars['other_contribution'] = p.other_contribution
			p.participant.vars['punish'] = p.punish
			p.participant.vars['timeout_MyPage1'] = p.timeout_MyPage1
			#p.participant.vars['timeout_MyPage2'] = p.timeout_MyPage2


class Player(BasePlayer):
	inactive = models.PositiveIntegerField() # active flag
	timeout_MyPage1 = models.PositiveIntegerField(initial=0)
	#timeout_MyPage2 = models.PositiveIntegerField(initial=0) # remove

	decision_0 = models.CurrencyField(min=0, max=Constants.endowment/Constants.cost_rate)
	decision_1_5 = models.CurrencyField(min=0, max=Constants.endowment/Constants.cost_rate)
	decision_6_10 = models.CurrencyField(min=0, max=Constants.endowment/Constants.cost_rate)
	decision_11_15 = models.CurrencyField(min=0, max=Constants.endowment/Constants.cost_rate)
	decision_16_20 = models.CurrencyField(min=0, max=Constants.endowment/Constants.cost_rate)
	decision_21_25 = models.CurrencyField(min=0, max=Constants.endowment/Constants.cost_rate)
	decision_26_30 = models.CurrencyField(min=0, max=Constants.endowment/Constants.cost_rate)
	# players' punishing decision for each possible contribution range

	# player's actual punishment used
	punish = models.CurrencyField(min=0, max=Constants.endowment)

	# others' punishment decisions
	other_contribution = models.PositiveIntegerField()
	self_paid = models.PositiveIntegerField()  # player's decision implemented or not

	score = models.FloatField()

	def creating_score(self):
		if self.inactive >= self.session.config['inactive_threshold']:
			self.score = 1
		else:
			self.score = random.random()

class Link(BaseLink):
	pass