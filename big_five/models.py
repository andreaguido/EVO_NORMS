from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, BaseLink,
	Currency as c, currency_range
)


author = 'Aron Szekely'

doc = """
The Big Five questionnaire from:
(1) John, O. P., Naumann, L. P., & Soto, C. J. (2008). Paradigm Shift to the Integrative Big-Five Trait Taxonomy: History, Measurement, and Conceptual Issues. In O. P. John, R. W. Robins, & L. A. Pervin (Eds.), Handbook of personality: Theory and research (pp. 114-158). New York, NY: Guilford Press.
(2) John, O. P., Donahue, E. M., & Kentle, R. L. (1991). The Big Five Inventory--Versions 4a and 54. Berkeley, CA: University of California,Berkeley, Institute of Personality and Social Research.
(3) Benet-Martinez, V., & John, O. P. (1998).  Los Cinco Grandes across cultures and ethnic groups: Multitrait multimethod analyses of the Big Five in Spanish and English.  Journal of Personality and Social Psychology, 75, 729-750.
"""


class Constants(BaseConstants):
	name_in_url = 'page_bi'
	players_per_group = None
	num_rounds = 1
	#would be nice to include multi-language support: language = "English"


class Subsession(BaseSubsession):
	pass

class Group(BaseGroup):
	pass


class Player(BasePlayer):
	timeout_IntroClimateExperiment = models.PositiveIntegerField(initial=0)
	timeout_MyPage = models.PositiveIntegerField(initial=0)

	q1 = models.PositiveIntegerField(
			verbose_name="Es muy hablador:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q2 = models.PositiveIntegerField(
		verbose_name="Tiende a ser criticón:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q3 = models.PositiveIntegerField(
		verbose_name="Es minucioso en el trabajo:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q4 = models.PositiveIntegerField(
		verbose_name="Es depresivo, melancólico:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q5 = models.PositiveIntegerField(
		verbose_name="Es original, se le ocurren ideas nuevas:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q6 = models.PositiveIntegerField(
		verbose_name="Es reservado:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q7 = models.PositiveIntegerField(
		verbose_name="Es generoso y ayuda a los demás:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q8 = models.PositiveIntegerField(
		verbose_name="Puede a veces ser algo descuidado:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q9 = models.PositiveIntegerField(
		verbose_name="Es calmado, controla bien el estrés:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q10 = models.PositiveIntegerField(
		verbose_name="Tiene intereses muy diversos:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q11 = models.PositiveIntegerField(
		verbose_name="Está lleno de energía:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q12 = models.PositiveIntegerField(
		verbose_name="Inicia disputas con los demás:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q13 = models.PositiveIntegerField(
		verbose_name="Es un trabajador cumplidor, digno de confianza:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q14 = models.PositiveIntegerField(
		verbose_name="Con frecuencia se pone tenso:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q15 = models.PositiveIntegerField(
		verbose_name="Es ingenioso, analítico:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q16 = models.PositiveIntegerField(
		verbose_name="Irradia entusiasmo:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q17 = models.PositiveIntegerField(
		verbose_name="Es indulgente, no le cuesta perdonar:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q18 = models.PositiveIntegerField(
		verbose_name="Tiende a ser desorganizado:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q19 = models.PositiveIntegerField(
		verbose_name="Se preocupa mucho por las cosas:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q20 = models.PositiveIntegerField(
		verbose_name="Tiene una imaginación activa:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q21 = models.PositiveIntegerField(
		verbose_name="Tiene a ser callado:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q22 = models.PositiveIntegerField(
		verbose_name="Es generalmente confiado:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q23 = models.PositiveIntegerField(
		verbose_name="Tiende a ser perezoso, vago:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q24 = models.PositiveIntegerField(
		verbose_name="Es emocionalmente estable, difícil de alterar:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q25 = models.PositiveIntegerField(
		verbose_name="Es inventivo:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q26 = models.PositiveIntegerField(
		verbose_name="Es asertivo, no teme expresar lo que quiere:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q27 = models.PositiveIntegerField(
		verbose_name="Es a veces frío y distante:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q28 = models.PositiveIntegerField(
		verbose_name="Persevera hasta terminar el trabajo:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q29 = models.PositiveIntegerField(
		verbose_name="Es temperamental, de humor cambiante:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q30 = models.PositiveIntegerField(
		verbose_name="Valora lo artístico, lo estético:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q31 = models.PositiveIntegerField(
		verbose_name="Es a veces tímido, inhibido:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q32 = models.PositiveIntegerField(
		verbose_name="Es considerado y amable con casi todo el mundo:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q33 = models.PositiveIntegerField(
		verbose_name="Hace las cosas de manera eficíente:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q34 = models.PositiveIntegerField(
		verbose_name="Mantiene la calma en situaciones difíciles:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q35 = models.PositiveIntegerField(
		verbose_name="Prefiere trabajos que son rutinarios:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q36 = models.PositiveIntegerField(
		verbose_name="Es extrovertido, sociable:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q37 = models.PositiveIntegerField(
		verbose_name="Es a veces maleducado con los demás:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q38 = models.PositiveIntegerField(
		verbose_name="Hace planes y los sigue cuidadosamente:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q39 = models.PositiveIntegerField(
		verbose_name="Se pone nervioso con facilidad:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q40 = models.PositiveIntegerField(
		verbose_name="Le gusta reflexionar, jugar con las ideas:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q41 = models.PositiveIntegerField(
		verbose_name="Tiene pocos intereses artísticos:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q42 = models.PositiveIntegerField(
		verbose_name="Le gusta cooperar con los demás:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q43 = models.PositiveIntegerField(
		verbose_name="Se distrae con facilidad:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	q44 = models.PositiveIntegerField(
		verbose_name="Es educado en arte, música, o literatura:",
		choices=[
			[1, "Muy en desacuerdo"],
			[2, "Ligeramente en desacuerdo"],
			[3, "Ni de acuerdo ni en desacuerdo"],
			[4, "Ligeramente de acuerdo"],
			[5, "Muy de acuerdo"],
		]
	)

	extraversion = models.PositiveIntegerField()
	agreeableness = models.PositiveIntegerField()
	conscientiousness = models.PositiveIntegerField()
	neuroticism = models.PositiveIntegerField()
	openness = models.PositiveIntegerField()

	def calc_score(self):
		self.extraversion = self.q1 + (6-self.q6) + self.q11 + self.q16 + (6-self.q21) + self.q26 + (6-self.q31) + self.q36
		self.agreeableness = (6-self.q2) + self.q7 + (6-self.q12) + self.q17 + self.q22 + (6-self.q27) + self.q32 + (6-self.q37) + self.q42
		self.conscientiousness = self.q3 + (6-self.q8) + self.q13 + (6-self.q18) + (6-self.q23) + self.q28 + self.q33 + self.q38 + (6-self.q43)
		self.neuroticism = self.q4 + (6-self.q9) + self.q14 + self.q19 + (6-self.q24) + self.q29 + (6-self.q34) + self.q39
		self.openness = self.q5 + self.q10 + self.q15 + self.q20 + self.q25 + self.q30 + (6-self.q35) + self.q40 + (6-self.q41) + self.q44


class Link(BaseLink):
	pass