from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import datetime


class IntroClimateExperiment(Page):
	timer_text = 'Tiempo restante para completar sus decisiones:'

	def set_extra_attributes(self):
		self.timeout_seconds = (self.session.config['start_datetime'] + datetime.timedelta(seconds=self.session.config['seconds_per_round']) - datetime.datetime.utcnow()).total_seconds()

#	XXX def get_timeout_seconds(self):
#		self.participant.vars['expiry'] = self.session.config['start_datetime'] + datetime.timedelta(seconds=self.session.config['seconds_per_round'])
#		#print("This is EXPIRY ", self.participant.vars['expiry'])
#		#print("this is TIME now ", datetime.datetime.utcnow())
#		#print("This is what is DISPLAYED ", (self.participant.vars['expiry'] - datetime.datetime.utcnow()).total_seconds())
#		return (self.participant.vars['expiry'] - datetime.datetime.utcnow()).total_seconds()

	def vars_for_template(self):
		return {
			'inactive_threshold': self.session.config['inactive_threshold'],
			'email': self.session.config['email'],
			'num_subjects_win': self.session.config['num_subjects_win'],
			'win_multiplier': self.session.config['win_multiplier'],
			'days': self.session.config['days'],
			'rate': self.session.config['puntos_euro_rate']
			}

	def before_next_page(self):
		if self.timeout_happened:
			self.player.timeout_IntroClimateExperiment = 1


class MyPage(Page):
	form_model = models.Player
	form_fields = ["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10", "q11", "q12", "q13", "q14", "q15", "q16", "q17", "q18", "q19", "q20", "q21", "q22", "q23", "q24", "q25", "q26", "q27", "q28", "q29", "q30", "q31", "q32", "q33", "q34", "q35", "q36", "q37", "q38", "q39", "q40", "q41", "q42", "q43", "q44"]
	timer_text = 'Tiempo restante para completar sus decisiones:'

#	XXX def get_timeout_seconds(self):
#		return (self.participant.vars['expiry'] - datetime.datetime.utcnow()).total_seconds()
	def set_extra_attributes(self):
		self.timeout_seconds = (self.session.config['start_datetime'] + datetime.timedelta(seconds=self.session.config['seconds_per_round']) - datetime.datetime.utcnow()).total_seconds()

	def vars_for_template(self):
		return {'email': self.session.config['email'],
				}

	def before_next_page(self):
		self.player.calc_score()
		if self.timeout_happened:
			self.player.timeout_MyPage = 1


class ResultsWaitPage(WaitPage):
	pass


class Results(Page):
	pass


page_sequence = [
	IntroClimateExperiment,
	MyPage,
]
