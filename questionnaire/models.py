from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range
)


author = 'Aron Szekely'

doc = """
Questionnaire
"""


class Constants(BaseConstants):
	name_in_url = 'page_qu'
	players_per_group = None
	num_rounds = 1

	text_Inactive = 'questionnaire/text_Inactive.html'


class Subsession(BaseSubsession):
	pass


class Group(BaseGroup):
	pass


class Player(BasePlayer):
	inactive = models.PositiveIntegerField()
	timeout_MyPage = models.PositiveIntegerField(initial=0)
	
	age = models.PositiveIntegerField(
		verbose_name="What is your age?",
		min=16,
		max=100,
		)

	gender = models.PositiveIntegerField(
		verbose_name="What gender do you identify as?",
		choices=[
			[0, "Male"],
			[1, "Female"],
			[2, "Other"],
		]
	)

	student = models.PositiveIntegerField(
		verbose_name="Are you currently a student?",
		choices=[
			[0, "No"],
			[1, "Yes"],
		]
	)

	discipline = models.StringField(
		verbose_name="If you answered yes to the above question, what subject do you study?",
		blank=True,
	)

	left_right = models.IntegerField(
		verbose_name="Where do you place yourself on a political spectrum from left to right wing?",
		choices=[
			[1, ""],
			[2, ""],
			[3, ""],
			[4, ""],
			[5, ""],
			[6, ""],
			[7, ""],
		],
		widget=widgets.RadioSelectHorizontal
	)
	
	experience = models.PositiveIntegerField(
		verbose_name="How many other experiments of this kind have you participated in?",
		min=0,
		max=100,
		)