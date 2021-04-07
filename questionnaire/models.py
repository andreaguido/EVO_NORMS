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
		verbose_name="Cuál es su edad?",
		min=16,
		max=100,
		)

	gender = models.PositiveIntegerField(
		verbose_name="Con qué género se identifica?",
		choices=[
			[0, "Masculino"],
			[1, "Femenino"],
			[2, "Otro"],
		]
	)

	student = models.PositiveIntegerField(
		verbose_name="Es usted actualmente un estudiante?",
		choices=[
			[0, "No"],
			[1, "Si"],
		]
	)

	discipline = models.StringField(
		verbose_name="Si ha respondido afirmativamente a la pregunta anterior, qué estudia?",
		blank=True,
	)

	left_right = models.IntegerField(
		verbose_name="Dónde se sitúa en un espectro político de izquierda a derecha?",
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
		verbose_name="En cuántos otros experimentos de este tipo ha participado?",
		min=0,
		max=100,
		)