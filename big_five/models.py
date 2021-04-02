from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, #BaseLink,
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
			verbose_name="Is talkative:",
			choices=[
				[1, "Disagree strongly"],
				[2, "Disagree a little"],
				[3, "Neither agree nor disagree"],
				[4, "Agree a little"],
				[5, "Agree strongly"],
			]
		)

	q2 = models.PositiveIntegerField(
		verbose_name="Tends to find fault with others:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q3 = models.PositiveIntegerField(
		verbose_name="Does a thorough job:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q4 = models.PositiveIntegerField(
		verbose_name="Is depressed, blue:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q5 = models.PositiveIntegerField(
		verbose_name="Is original, comes up with new ideas:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q6 = models.PositiveIntegerField(
		verbose_name="Is reserved:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q7 = models.PositiveIntegerField(
		verbose_name="Is helpful and unselfish with others:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q8 = models.PositiveIntegerField(
		verbose_name="Can be somewhat careless:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q9 = models.PositiveIntegerField(
		verbose_name="Is relaxed, handles stress well:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q10 = models.PositiveIntegerField(
		verbose_name="Is curious about many different things:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q11 = models.PositiveIntegerField(
		verbose_name="Is full of energy:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q12 = models.PositiveIntegerField(
		verbose_name="Starts quarrels with others:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q13 = models.PositiveIntegerField(
		verbose_name="Is a reliable worker:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q14 = models.PositiveIntegerField(
		verbose_name="Can be tense:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q15 = models.PositiveIntegerField(
		verbose_name="Is ingenious, a deep thinker:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q16 = models.PositiveIntegerField(
		verbose_name="Generates a lot of enthusiasm:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q17 = models.PositiveIntegerField(
		verbose_name="Has a forgiving nature:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q18 = models.PositiveIntegerField(
		verbose_name="Tends to be disorganised:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q19 = models.PositiveIntegerField(
		verbose_name="Worries a lot:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q20 = models.PositiveIntegerField(
		verbose_name="Has an active imagination:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q21 = models.PositiveIntegerField(
		verbose_name="Tends to be quiet:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q22 = models.PositiveIntegerField(
		verbose_name="Is generally trusting:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q23 = models.PositiveIntegerField(
		verbose_name="Tends to be lazy:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q24 = models.PositiveIntegerField(
		verbose_name="Is emotionally stable, not easily upset:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q25 = models.PositiveIntegerField(
		verbose_name="Is inventive:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q26 = models.PositiveIntegerField(
		verbose_name="Has an assertive personality:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q27 = models.PositiveIntegerField(
		verbose_name="Can be cold and aloof:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q28 = models.PositiveIntegerField(
		verbose_name="Perseveres until the task is finished:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q29 = models.PositiveIntegerField(
		verbose_name="Can be moody:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q30 = models.PositiveIntegerField(
		verbose_name="Values artistic, aesthetic experiences:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q31 = models.PositiveIntegerField(
		verbose_name="Is sometimes shy, inhibited:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q32 = models.PositiveIntegerField(
		verbose_name="Is considerate and kind to almost everyone:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q33 = models.PositiveIntegerField(
		verbose_name="Does things efficiently:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q34 = models.PositiveIntegerField(
		verbose_name="Remains calm in tense situations:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q35 = models.PositiveIntegerField(
		verbose_name="Prefers work that is routine:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q36 = models.PositiveIntegerField(
		verbose_name="Is outgoing, sociable:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q37 = models.PositiveIntegerField(
		verbose_name="Is sometimes rude to others:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q38 = models.PositiveIntegerField(
		verbose_name="Makes plans and follows through with them:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q39 = models.PositiveIntegerField(
		verbose_name="Gets nervous easily:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q40 = models.PositiveIntegerField(
		verbose_name="Likes to reflect, play with ideas:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q41 = models.PositiveIntegerField(
		verbose_name="Has few artistic interests:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q42 = models.PositiveIntegerField(
		verbose_name="Likes to cooperate with others:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q43 = models.PositiveIntegerField(
		verbose_name="Is easily distracted:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
		]
	)

	q44 = models.PositiveIntegerField(
		verbose_name="Is sophisticated in art, music, or literature:",
		choices=[
			[1, "Disagree strongly"],
			[2, "Disagree a little"],
			[3, "Neither agree nor disagree"],
			[4, "Agree a little"],
			[5, "Agree strongly"],
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


#class Link(BaseLink):
#	pass