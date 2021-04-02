from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range
)

import random

author = 'Aron Szekely'

doc = """
Implementation of risk preference elicitation method from Eckel and Grossman 2002. Sex differences and statistical stereotyping in attitudes toward financial risk. 
Specifically from Dave et al. 2010. Eliciting risk preferences: When is simple better? (see Appendix)
"""


class Constants(BaseConstants):
	name_in_url = 'page_ri_eg'
	players_per_group = None
	num_rounds = 1

	choice_1_high = 28
	choice_2_high = 36
	choice_3_high = 44
	choice_4_high = 52
	choice_5_high = 60
	choice_6_high = 70
	
	choice_1_low = 28
	choice_2_low = 24
	choice_3_low = 20
	choice_4_low = 16
	choice_5_low = 12
	choice_6_low = 2


class Subsession(BaseSubsession):
	pass


class Group(BaseGroup):
	pass


class Player(BasePlayer):
	timeout_MyPage = models.PositiveIntegerField(initial=0)

	choice = models.PositiveIntegerField(
		choices=[
			[0, "Gamble 1"],
			[1, "Gamble 2"],
			[2, "Gamble 3"],
			[3, "Gamble 4"],
			[4, "Gamble 5"],
			[5, "Gamble 6"],
		]
	)

	lottery_win = models.FloatField(default=0)
		
	def calc_pay(self):
		self.participant.vars['lottery_choice'] = self.choice

		self.lottery_win = random.randint(0, 1)
		self.participant.vars['lottery_win'] = self.lottery_win
		
		list_high = [Constants.choice_1_high, Constants.choice_2_high, Constants.choice_3_high, Constants.choice_4_high, Constants.choice_5_high, Constants.choice_6_high,]
		
		list_low = [Constants.choice_1_low, Constants.choice_2_low, Constants.choice_3_low, Constants.choice_4_low, Constants.choice_5_low, Constants.choice_6_low,]
		
		if self.lottery_win == 1:
			self.payoff = list_high[self.choice]
		else:
			self.payoff = list_low[self.choice]

		self.participant.vars['risk_lottery_payoff'] = self.payoff