from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import datetime

#class Page(Page):

#    def set_mail(self):
#           self.timeout_mailing_seconds = 5 #seg después de cargar la pagina
#          self.mail_body_text = "IBSEN: El experimento ha comenzado."

# OK
class Initialisation(Page):
	timeout_seconds = 1

	def before_next_page(self): # this function is used to bring participants values from previous apps
		self.player.inactive = self.participant.vars['inactive']
		#if self.participant.id_in_session < 10:
			#self.player.inactive = 0
		# remove the above two lines: only for testing
		self.player.timeout_already_happened = 0
		self.player.creating_score()
		self.participant.vars['score'] = self.player.score

# OK
class ShuffleWaitPage(WaitPage):
	wait_for_all_groups = True

	def after_all_players_arrive(self):
		# stranger matching protocol
		# notes: score is the variable that identifies inactive players
		sorted_players = sorted(
			self.subsession.get_players(),
			key=lambda player: player.participant.vars['score']
		)
		group_matrix = []
		ppg = Constants.players_per_group
		for i in range(0, len(sorted_players), ppg):
			group_matrix.append(sorted_players[i:i+ppg])
		self.subsession.set_group_matrix(group_matrix)
		print(group_matrix)

# OK
class Instructions(Page):
	timer_text = Constants.timer_text

	def is_displayed(self):
		return self.round_number == 1

	def vars_for_template(self):
		return {
			'inactive_threshold': self.session.config['inactive_threshold'],
			'email': self.session.config['email'],
			'num_subjects_win': self.session.config['num_subjects_win'],
			'win_multiplier': self.session.config['win_multiplier'],
			'type': "XXX",
            'rounds': Constants.num_rounds
		}

	def get_timeout_seconds(self):
		self.participant.vars['expiry'] = self.session.config['start_datetime'] + datetime.timedelta(seconds=self.session.config['seconds_per_round']*(self.round_number+1))
		return (self.participant.vars['expiry'] - datetime.datetime.utcnow()).total_seconds()

	def before_next_page(self):
		if self.timeout_happened:
			self.player.timeout_Instructions = 1

# OK
class Example(Page):
	timer_text = Constants.timer_text

	def is_displayed(self):
		return self.round_number == 1

	def vars_for_template(self):
		return {
			'no_spending': Constants.endowment*0,
			'one_quarter_spending': Constants.endowment*1/4,
			'half_spending': Constants.endowment*1/2,
			'three_quarters_spending': Constants.endowment*3/4,
			'full_spending': Constants.endowment,
			'sum1': Constants.other_players_per_group * Constants.endowment*1/2,
			'sum2': Constants.players_per_group_display * Constants.endowment*3/4,
			'inactive_threshold': self.session.config['inactive_threshold'],
			'email': self.session.config['email'],
			'num_subjects_win': self.session.config['num_subjects_win'],
			'win_multiplier': self.session.config['win_multiplier'],
            'rounds': Constants.num_rounds
		}

	def get_timeout_seconds(self):
		return (self.participant.vars['expiry'] - datetime.datetime.utcnow()).total_seconds()

	def before_next_page(self):
		if self.timeout_happened:
			self.player.timeout_Example = 1

# OK
class Control(Page):
	form_model = models.Player
	form_fields = ['question_1_1', 'question_1_2', 'question_2_1', 'question_2_2', 'question_3_1', 'question_3_2', 'question_4_1', 'question_4_2', 'question_5']
	timer_text = Constants.timer_text

	def is_displayed(self):
		return self.round_number == 1

	def vars_for_template(self):
		return {
			'inactive_threshold': self.session.config['inactive_threshold'],
			'email': self.session.config['email'],
			'num_subjects_win': self.session.config['num_subjects_win'],
			'win_multiplier': self.session.config['win_multiplier'],
            'rounds': Constants.num_rounds
		}

	def before_next_page(self):
		self.player.control_calc()
		if self.timeout_happened:
			self.player.timeout_Control = 1

	def get_timeout_seconds(self):
		return (self.participant.vars['expiry'] - datetime.datetime.utcnow()).total_seconds()

# OK
class Answers(Page):
	timer_text = Constants.timer_text

	def is_displayed(self):
		return self.round_number == 1

	def get_timeout_seconds(self):
		return (self.participant.vars['expiry'] - datetime.datetime.utcnow()).total_seconds()

	def vars_for_template(self):
		if self.player.question_1_1 == 0:
			question_1_1 = "25"
		elif self.player.question_1_1 == 1:
			question_1_1 = "15"
		elif self.player.question_1_1 == 2:
			question_1_1 = "5"

		if self.player.question_1_2 == 0:
			question_1_2 = "72.9"
		elif self.player.question_1_2 == 1:
			question_1_2 = "52.2"
		elif self.player.question_1_2 == 2:
			question_1_2 = "31.8"

		if self.player.question_2_1 == 0:
			question_2_1 = "25"
		elif self.player.question_2_1 == 1:
			question_2_1 = "15"
		elif self.player.question_2_1 == 2:
			question_2_1 = "5"

		if self.player.question_2_2 == 0:
			question_2_2 = "72.9"
		elif self.player.question_2_2 == 1:
			question_2_2 = "52.2"
		elif self.player.question_2_2 == 2:
			question_2_2 = "10.7"

		if self.player.question_3_1 == 0:
			question_3_1 = "22"
		elif self.player.question_3_1 == 1:
			question_3_1 = "5"
		elif self.player.question_3_1 == 2:
			question_3_1 = "2"

		if self.player.question_3_2 == 0:
			question_3_2 = "6.3"
		elif self.player.question_3_2 == 1:
			question_3_2 = "354.9"
		elif self.player.question_3_2 == 2:
			question_3_2 = "14"


		if self.player.question_4_1 == 0:
			question_4_1 = "2"
		elif self.player.question_4_1 == 1:
			question_4_1 = "6"
		elif self.player.question_4_1 == 2:
			question_4_1 = "15"

		if self.player.question_4_2 == 0:
			question_4_2 = "6.3"
		elif self.player.question_4_2 == 1:
			question_4_2 = "150.4"
		elif self.player.question_4_2 == 2:
			question_4_2 = "14"


		return {
			'q_1_1': question_1_1,
			'q_1_2': question_1_2,
			'q_2_1': question_2_1,
			'q_2_2': question_2_2,
			'q_3_1': question_3_1,
			'q_3_2': question_3_2,
			'q_4_1': question_4_1,
			'q_4_2': question_4_2,
			'a11': 25,
			'a12': 72.9,
			'a21': 25,
			'a22': 10.7,
			'a31': 2,
			'a32': 354.9,
			'a41': 2,
			'a42': 6.3,
			'inactive_threshold': self.session.config['inactive_threshold'],
			'email': self.session.config['email'],
			'num_subjects_win': self.session.config['num_subjects_win'],
			'win_multiplier': self.session.config['win_multiplier'],
			'rounds': self.round_number
		}

	def before_next_page(self):
		if self.timeout_happened:
			self.player.timeout_Answers = 1

########
# LATER #
class PreviousResults(Page):
	timer_text = Constants.timer_text

	def is_displayed(self):
		return self.round_number > 1 
	
	def get_timeout_seconds(self):	
		self.participant.vars['expiry'] = self.session.config['start_datetime'] + datetime.timedelta(seconds=self.session.config['seconds_per_round']*(self.round_number+1))
		return (self.participant.vars['expiry'] - datetime.datetime.utcnow()).total_seconds()

	def vars_for_template(self):
		return {
			'display_payoff': self.participant.vars['unconditional_payoff'],
			'inactive_threshold': self.session.config['inactive_threshold'],
			'previous_round_number': self.participant.vars['previous_round_number'],
			'previous_contribution': self.participant.vars['contribution'],
			'previous_total_contribution': self.participant.vars['total_contribution'],
			#'previous_unconditional_disaster_value': self.participant.vars['unconditional_disaster_value'],
			#'previous_unconditional_disaster_value_display': self.participant.vars['unconditional_disaster_value_display'],
			#'previous_disaster_probability': self.participant.vars['disaster_probability'],
#			'previous_conditional_contribution': self.participant.vars['conditional_contribution'],
#			'previous_conditional_total_contribution': self.participant.vars['conditional_total_contribution'],
#			'previous_conditional_disaster_value': self.participant.vars['conditional_disaster_value'],
#			'previous_conditional_disaster_value_display': self.participant.vars['conditional_disaster_value_display'],
			'previous_unconditional_payoff': self.participant.vars['unconditional_payoff'],
#			'previous_conditional_payoff': self.participant.vars['conditional_payoff'],
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
#########

# OK
class Preparation(Page):
	timer_text = Constants.timer_text

	def get_timeout_seconds(self):
		return (self.participant.vars['expiry'] - datetime.datetime.utcnow()).total_seconds()

	def vars_for_template(self):
			return {
				'diff_group_rounds': self.session.vars['diff_group_rounds'],
				'inactive_threshold': self.session.config['inactive_threshold'],
				'days_completed': (self.round_number + 1)/2,
				'days_total': (Constants.num_rounds + 2)/2,
				'email': self.session.config['email'],
				'num_subjects_win': self.session.config['num_subjects_win'],
				'win_multiplier': self.session.config['win_multiplier'],
				'rounds': Constants.num_rounds
				}
			
	def before_next_page(self):
		self.player.payment_rounds()
		if self.timeout_happened:
			self.player.timeout_Preparation = 1

# OK
class Beliefs_before_PNB(Page):
	form_model = models.Player
	form_fields = ['personal_normative_beliefs']
	timer_text = Constants.timer_text

	def get_timeout_seconds(self):
		return (self.participant.vars['expiry'] - datetime.datetime.utcnow()).total_seconds()

	def vars_for_template(self):
		return {
			'inactive_threshold': self.session.config['inactive_threshold'],
			'email': self.session.config['email'],
			'num_subjects_win': self.session.config['num_subjects_win'],
			'win_multiplier': self.session.config['win_multiplier'],
			'rounds': self.round_number
		}

	def before_next_page(self):
		if self.timeout_happened:
			self.player.timeout_Beliefs_before_PNB = 1
			self.player.inactive_pnb()

# OK
class Beliefs_before_EE(Page):
	form_model = models.Player
	timer_text = Constants.timer_text
	
	def get_form_fields(self):
		return ['empirical_expectations{}'.format(i) for i in range(0, Constants.other_players_per_group)]
	
	def get_timeout_seconds(self):
		return (self.participant.vars['expiry'] - datetime.datetime.utcnow()).total_seconds()
	
	def vars_for_template(self):
		return {
			'inactive_threshold': self.session.config['inactive_threshold'],
			'max_ee_earning': Constants.belief_correct_pay * Constants.other_players_per_group,
			'email': self.session.config['email'],
			'num_subjects_win': self.session.config['num_subjects_win'],
			'win_multiplier': self.session.config['win_multiplier'],
			'rounds': self.round_number
		}

	def before_next_page(self):
		if self.timeout_happened:
			self.player.empirical_expectations0 = 0
			self.player.empirical_expectations1 = 0
			self.player.empirical_expectations2 = 0
			self.player.empirical_expectations3 = 0
			self.player.empirical_expectations4 = 0
			self.player.timeout_Beliefs_before_EE = 1

	def error_message(self, values):
		if Constants.other_players_per_group == 2:
			if values["empirical_expectations0"] < values["empirical_expectations1"]:
				return "Please ensure that your inputs are orderer from high to low such that the highest number is in the top row and the lowest in the bottom"

		if Constants.other_players_per_group == 3:
			if values["empirical_expectations0"] < values["empirical_expectations1"] or values["empirical_expectations0"] < values["empirical_expectations2"] or values["empirical_expectations1"] < values["empirical_expectations2"]:
				return "Please ensure that your inputs are orderer from high to low such that the highest number is in the top row and the lowest in the bottom"

		if Constants.other_players_per_group == 4:
			if values["empirical_expectations0"] < values["empirical_expectations1"] or values["empirical_expectations0"] < values["empirical_expectations2"] or values["empirical_expectations0"] < values["empirical_expectations3"] or values["empirical_expectations1"] < values["empirical_expectations2"]	or values["empirical_expectations1"] < values["empirical_expectations3"] or values["empirical_expectations2"] < values["empirical_expectations3"]:
				return "Please ensure that your inputs are orderer from high to low such that the highest number is in the top row and the lowest in the bottom"
			
		if Constants.other_players_per_group == 5:
			if values["empirical_expectations0"] < values["empirical_expectations1"] or values["empirical_expectations0"] < values["empirical_expectations2"] or values["empirical_expectations0"] < values["empirical_expectations3"] or values["empirical_expectations0"] < values["empirical_expectations4"] or values["empirical_expectations1"] < values["empirical_expectations2"] or values["empirical_expectations1"] < values["empirical_expectations3"] or values["empirical_expectations1"] < values["empirical_expectations4"] or values["empirical_expectations2"] < values["empirical_expectations3"] or values["empirical_expectations2"] < values["empirical_expectations4"] or values["empirical_expectations3"] < values["empirical_expectations4"]:
				return "Please ensure that your inputs are orderer from high to low such that the highest number is in the top row and the lowest in the bottom"

# OK
class Beliefs_before_NE(Page):
	form_model = models.Player
	timer_text = Constants.timer_text

	def get_form_fields(self):
		return ['normative_expectations{}'.format(i) for i in range(0, Constants.other_players_per_group)]

	def get_timeout_seconds(self):
		return (self.participant.vars['expiry'] - datetime.datetime.utcnow()).total_seconds()

	def vars_for_template(self):
		return {
			'inactive_threshold': self.session.config['inactive_threshold'],
			'max_ne_earning': Constants.belief_correct_pay * Constants.other_players_per_group,
			'email': self.session.config['email'],
			'num_subjects_win': self.session.config['num_subjects_win'],
			'win_multiplier': self.session.config['win_multiplier'],
			'rounds': self.round_number
		}

	def before_next_page(self):
		if self.timeout_happened:
			self.player.normative_expectations0 = 0
			self.player.normative_expectations1 = 0
			self.player.normative_expectations2 = 0
			self.player.normative_expectations3 = 0
			self.player.normative_expectations4 = 0
			self.player.timeout_Beliefs_before_NE = 1

	def error_message(self, values):
		if Constants.other_players_per_group == 2:
			if values["normative_expectations0"] < values["normative_expectations1"]:
				return "Please ensure that your inputs are orderer from high to low such that the highest number is in the top row and the lowest in the bottom"

		if Constants.other_players_per_group == 3:
			if values["normative_expectations0"] < values["normative_expectations1"] or values["normative_expectations0"] < values["normative_expectations2"] or values["normative_expectations1"] < values["normative_expectations2"]:
				return "Please ensure that your inputs are orderer from high to low such that the highest number is in the top row and the lowest in the bottom"

		if Constants.other_players_per_group == 4:
			if values["normative_expectations0"] < values["normative_expectations1"] or values["normative_expectations0"] < values["normative_expectations2"] or values["normative_expectations0"] < values["normative_expectations3"] or values["normative_expectations1"] < values["normative_expectations2"]	or values["normative_expectations1"] < values["normative_expectations3"] or values["normative_expectations2"] < values["normative_expectations3"]:
				return "Please ensure that your inputs are orderer from high to low such that the highest number is in the top row and the lowest in the bottom"
			
		if Constants.other_players_per_group == 5:
			if values["normative_expectations0"] < values["normative_expectations1"] or values["normative_expectations0"] < values["normative_expectations2"] or values["normative_expectations0"] < values["normative_expectations3"] or values["normative_expectations0"] < values["normative_expectations4"] or values["normative_expectations1"] < values["normative_expectations2"] or values["normative_expectations1"] < values["normative_expectations3"] or values["normative_expectations1"] < values["normative_expectations4"] or values["normative_expectations2"] < values["normative_expectations3"] or values["normative_expectations2"] < values["normative_expectations4"] or values["normative_expectations3"] < values["normative_expectations4"]:
				return "Please ensure that your inputs are orderer from high to low such that the highest number is in the top row and the lowest in the bottom"

# OK
class Contribute_uncond(Page):
	form_model = models.Player
	form_fields = ['contribution']
	timer_text = Constants.timer_text

	def get_timeout_seconds(self):
		return (self.participant.vars['expiry'] - datetime.datetime.utcnow()).total_seconds()

	def vars_for_template(self):
		return {
			'inactive_threshold': self.session.config['inactive_threshold'],
			'email': self.session.config['email'],
			'num_subjects_win': self.session.config['num_subjects_win'],
			'win_multiplier': self.session.config['win_multiplier'],
			'rounds': self.round_number,
			'par_a': Constants.p_a,
			'par_b': Constants.p_b,
		}

	def before_next_page(self):
		if self.timeout_happened:
			self.player.timeout_already_happened = 1
			self.player.timeout_Contribute_uncond = 1
			self.player.inactive_contribution()

## NOT USED ##  DELETE
#class Contribute_cond(Page):
#	form_model = models.Player
#	form_fields = ['contribution_hh', 'contribution_hl', 'contribution_lh', 'contribution_ll']
#	timer_text = Constants.timer_text
#
#	def is_displayed(self):
#		return self.round_number in Constants.uncond_cond_rounds
#
#	def get_timeout_seconds(self):
#		return (self.participant.vars['expiry'] - datetime.datetime.utcnow()).total_seconds()
#
#	def vars_for_template(self):
#		return {
#			'half_spending': Constants.endowment*1/2,
#			'half_players': Constants.players_per_group/2,
#			'inactive_threshold': self.session.config['inactive_threshold'],
#			'email': self.session.config['email'],
#			'num_subjects_win': self.session.config['num_subjects_win'],
#			'win_multiplier': self.session.config['win_multiplier'],
#			'rounds': self.round_number
#		}
#
#	def before_next_page(self):
#		if self.timeout_happened:
#			self.player.timeout_already_happened = 1
#			self.player.timeout_Contribute_cond = 1


#class Beliefs_after_PNB(Page):
#	form_model = models.Player
#	form_fields = ['personal_normative_beliefs']
#	timer_text = Constants.timer_text
#
#	def is_displayed(self):
#		return self.player.belief_elicit_before == 0 and self.round_number in Constants.PNB_NE_rounds
#
#	def get_timeout_seconds(self):
#		return (self.participant.vars['expiry'] - datetime.datetime.utcnow()).total_seconds()
#
#	def vars_for_template(self):
#		return {
#			'inactive_threshold': self.session.config['inactive_threshold'],
#			'email': self.session.config['email'],
#			'num_subjects_win': self.session.config['num_subjects_win'],
#			'win_multiplier': self.session.config['win_multiplier'],
#		}
#
#	def before_next_page(self):
#		if self.timeout_happened:
#			self.player.timeout_already_happened = 1
#			self.player.timeout_Beliefs_after_PNB = 1
#			self.player.inactive_pnb()
#
#class Beliefs_after_EE(Page):
#	form_model = models.Player
#	timer_text = Constants.timer_text
#
#	def get_form_fields(self):
#		return ['empirical_expectations{}'.format(i) for i in range(0, Constants.other_players_per_group)]
#
#	def is_displayed(self):
#		return self.player.belief_elicit_before == 0
#
#	def get_timeout_seconds(self):
#		return (self.participant.vars['expiry'] - datetime.datetime.utcnow()).total_seconds()
#
#	def vars_for_template(self):
#		return {
#			'inactive_threshold': self.session.config['inactive_threshold'],
#			'max_ee_earning': Constants.belief_correct_pay * Constants.other_players_per_group,
#			'email': self.session.config['email'],
#			'num_subjects_win': self.session.config['num_subjects_win'],
#			'win_multiplier': self.session.config['win_multiplier'],
#			}
#
#	def before_next_page(self):
#		if self.timeout_happened:
#			self.player.empirical_expectations0 = 0
#			self.player.empirical_expectations1 = 0
#			self.player.empirical_expectations2 = 0
#			self.player.empirical_expectations3 = 0
#			self.player.empirical_expectations4 = 0
#			self.player.timeout_already_happened = 1
#			self.player.timeout_Beliefs_after_EE = 1
#
#	def error_message(self, values):
#		if Constants.other_players_per_group == 2:
#			if values["empirical_expectations0"] < values["empirical_expectations1"]:
#				return "Please ensure that your inputs are orderer from high to low such that the highest number is in the top row and the lowest in the bottom"
#
#		if Constants.other_players_per_group == 3:
#			if values["empirical_expectations0"] < values["empirical_expectations1"] or values["empirical_expectations0"] < values["empirical_expectations2"] or values["empirical_expectations1"] < values["empirical_expectations2"]:
#				return "Please ensure that your inputs are orderer from high to low such that the highest number is in the top row and the lowest in the bottom"
#
#		if Constants.other_players_per_group == 4:
#			if values["empirical_expectations0"] < values["empirical_expectations1"] or values["empirical_expectations0"] < values["empirical_expectations2"] or values["empirical_expectations0"] < values["empirical_expectations3"] or values["empirical_expectations1"] < values["empirical_expectations2"]	or values["empirical_expectations1"] < values["empirical_expectations3"] or values["empirical_expectations2"] < values["empirical_expectations3"]:
#				return "Please ensure that your inputs are orderer from high to low such that the highest number is in the top row and the lowest in the bottom"
#
#		if Constants.other_players_per_group == 5:
#			if values["empirical_expectations0"] < values["empirical_expectations1"] or values["empirical_expectations0"] < values["empirical_expectations2"] or values["empirical_expectations0"] < values["empirical_expectations3"] or values["empirical_expectations0"] < values["empirical_expectations4"] or values["empirical_expectations1"] < values["empirical_expectations2"] or values["empirical_expectations1"] < values["empirical_expectations3"] or values["empirical_expectations1"] < values["empirical_expectations4"] or values["empirical_expectations2"] < values["empirical_expectations3"] or values["empirical_expectations2"] < values["empirical_expectations4"] or values["empirical_expectations3"] < values["empirical_expectations4"]:
#				return "Please ensure that your inputs are orderer from high to low such that the highest number is in the top row and the lowest in the bottom"
#
#
#class Beliefs_after_NE(Page):
#	form_model = models.Player
#	timer_text = Constants.timer_text
#
#	def get_form_fields(self):
#		return ['normative_expectations{}'.format(i) for i in range(0, Constants.other_players_per_group)]
#
#	def is_displayed(self):
#		return self.player.belief_elicit_before == 0 and self.round_number in Constants.PNB_NE_rounds
#
#	def get_timeout_seconds(self):
#		return (self.participant.vars['expiry'] - datetime.datetime.utcnow()).total_seconds()
#
#	def vars_for_template(self):
#		return {
#			'inactive_threshold': self.session.config['inactive_threshold'],
#			'max_ne_earning': Constants.belief_correct_pay * Constants.other_players_per_group,
#			'email': self.session.config['email'],
#			'num_subjects_win': self.session.config['num_subjects_win'],
#			'win_multiplier': self.session.config['win_multiplier'],
#		}
#
#	def before_next_page(self):
#		if self.timeout_happened:
#			self.player.normative_expectations0 = 0
#			self.player.normative_expectations1 = 0
#			self.player.normative_expectations2 = 0
#			self.player.normative_expectations3 = 0
#			self.player.normative_expectations4 = 0
#			self.player.timeout_already_happened = 1
#			self.player.timeout_Beliefs_after_NE = 1
#
#	def error_message(self, values):
#		if Constants.other_players_per_group == 2:
#			if values["normative_expectations0"] < values["normative_expectations1"]:
#				return "Please ensure that your inputs are orderer from high to low such that the highest number is in the top row and the lowest in the bottom"
#
#		if Constants.other_players_per_group == 3:
#			if values["normative_expectations0"] < values["normative_expectations1"] or values["normative_expectations0"] < values["normative_expectations2"] or values["normative_expectations1"] < values["normative_expectations2"]:
#				return "Please ensure that your inputs are orderer from high to low such that the highest number is in the top row and the lowest in the bottom"
#
#		if Constants.other_players_per_group == 4:
#			if values["normative_expectations0"] < values["normative_expectations1"] or values["normative_expectations0"] < values["normative_expectations2"] or values["normative_expectations0"] < values["normative_expectations3"] or values["normative_expectations1"] < values["normative_expectations2"]	or values["normative_expectations1"] < values["normative_expectations3"] or values["normative_expectations2"] < values["normative_expectations3"]:
#				return "Please ensure that your inputs are orderer from high to low such that the highest number is in the top row and the lowest in the bottom"
#
#		if Constants.other_players_per_group == 5:
#			if values["normative_expectations0"] < values["normative_expectations1"] or values["normative_expectations0"] < values["normative_expectations2"] or values["normative_expectations0"] < values["normative_expectations3"] or values["normative_expectations0"] < values["normative_expectations4"] or values["normative_expectations1"] < values["normative_expectations2"] or values["normative_expectations1"] < values["normative_expectations3"] or values["normative_expectations1"] < values["normative_expectations4"] or values["normative_expectations2"] < values["normative_expectations3"] or values["normative_expectations2"] < values["normative_expectations4"] or values["normative_expectations3"] < values["normative_expectations4"]:
#				return "Please ensure that your inputs are orderer from high to low such that the highest number is in the top row and the lowest in the bottom"

# OK
class WaitNextRound1(Page):
	timer_text = 'Thank you for making your decisions. You will be able to proceed with the experiment in:'

	def get_timeout_seconds(self):
		return (self.participant.vars['expiry'] - datetime.datetime.utcnow()).total_seconds()

	def vars_for_template(self):
		return {
			'inactive_threshold': self.session.config['inactive_threshold'],
			'email': self.session.config['email'],
			'num_subjects_win': self.session.config['num_subjects_win'],
			'win_multiplier': self.session.config['win_multiplier'],
			'rounds': self.round_number
		}

	def before_next_page(self):
		if self.timeout_happened and self.player.timeout_already_happened == 1:
			self.player.inactive = self.player.inactive + 1

# OK : need to have a waiting page here cause we need to wait for all participants to arrive.
class ResultsWaitPage1(WaitPage):
	pass


class WaitNextRound2(Page):
	timer_text = 'Thank you for making your decisions. You will be able to proceed with the experiment in:'
	timeout_seconds = 1

	def vars_for_template(self):
		return {
			'inactive_threshold': self.session.config['inactive_threshold'],
			'email': self.session.config['email'],
			'num_subjects_win': self.session.config['num_subjects_win'],
			'win_multiplier': self.session.config['win_multiplier'],
			'rounds': self.round_number
		}

	def before_next_page(self):
		self.player.other_contributions()
		self.player.empirical_expectations()
		self.player.normative_expectations()


class ResultsWaitPage2(WaitPage):

	def after_all_players_arrive(self):
		#self.group.norm_calc()
#		self.group.calc_disaster()
		self.group.set_payoffs()


class Results(Page):
	timeout_seconds = 1

	def vars_for_template(self):
		return {
			'display_payoff': self.player.unconditional_payoff,
			'inactive_threshold': self.session.config['inactive_threshold'],
			'email': self.session.config['email'],
			'num_subjects_win': self.session.config['num_subjects_win'],
			'win_multiplier': self.session.config['win_multiplier'],
		}

	def before_next_page(self):
		self.player.cumulative_payoff()
		self.participant.vars['previous_round_number'] = self.round_number
		self.participant.vars['inactive'] = self.player.inactive
		self.participant.vars['contribution'] = self.player.contribution
		self.participant.vars['total_contribution'] = self.group.total_contribution
		#self.participant.vars['unconditional_disaster_value'] = self.group.unconditional_disaster_value
		#self.participant.vars['unconditional_disaster_value_display'] = self.group.unconditional_disaster_value_display
		#self.participant.vars['conditional_total_contribution'] = self.player.conditional_total_contribution
		self.participant.vars['unconditional_payoff'] = self.player.unconditional_payoff
		self.participant.vars['other_contribution0'] = self.player.other_contribution0
		self.participant.vars['other_contribution1'] = self.player.other_contribution1
		self.participant.vars['other_contribution2'] = self.player.other_contribution2
		self.participant.vars['other_contribution3'] = self.player.other_contribution3
		self.participant.vars['other_contribution4'] = self.player.other_contribution4
		self.participant.vars['other_inactive0'] = self.player.other_inactive0
		self.participant.vars['other_inactive1'] = self.player.other_inactive1
		self.participant.vars['other_inactive2'] = self.player.other_inactive2
		self.participant.vars['other_inactive3'] = self.player.other_inactive3
		self.participant.vars['other_inactive4'] = self.player.other_inactive4
		self.participant.vars['other_timeout_Contribute0'] = self.player.other_timeout_Contribute0
		self.participant.vars['other_timeout_Contribute1'] = self.player.other_timeout_Contribute1
		self.participant.vars['other_timeout_Contribute2'] = self.player.other_timeout_Contribute2
		self.participant.vars['other_timeout_Contribute3'] = self.player.other_timeout_Contribute3
		self.participant.vars['other_timeout_Contribute4'] = self.player.other_timeout_Contribute4
		self.participant.vars['num_rounds'] = Constants.num_rounds
		self.participant.vars['endowment'] = Constants.endowment
		#self.participant.vars['uncond_cond_rounds'] = Constants.uncond_cond_rounds


page_sequence = [
	Initialisation,
	ShuffleWaitPage,
	Instructions,
	Example,
	Control,
	Answers,
	PreviousResults,
	Preparation,
	Beliefs_before_PNB,
	Beliefs_before_EE,
	Beliefs_before_NE,
	Contribute_uncond,
	#Contribute_cond,
	#Beliefs_after_PNB,
	#Beliefs_after_EE,
	#Beliefs_after_NE,
	WaitNextRound1,
	ResultsWaitPage1,
	WaitNextRound2,
	ResultsWaitPage2,
	Results
]