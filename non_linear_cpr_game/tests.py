from otree.api import Currency as c, currency_range
from . import views
from otree.api import Bot, SubmissionMustFail
from ._builtin import Bot
from .models import Constants
from otree.api import Submission
import random


class PlayerBot(Bot):

	def play_round(self):
		yield Submission(views.Initialisation, timeout_happened=True, check_html=False)

		if self.subsession.round_number == 1:
			yield Submission(views.Instructions, check_html=False)
			yield Submission(views.Example, check_html=False)
			yield Submission(views.Control, {'question_1_1': random.randint(0, 2), 'question_1_2': random.randint(0, 2),
											 'question_2_1': random.randint(0, 2), 'question_2_2': random.randint(0, 2),
											 'question_3_1': random.randint(0, 2), 'question_3_2': random.randint(0, 2),
											 'question_4_1': random.randint(0, 2), 'question_4_2': random.randint(0, 2),
											 'question_5': random.randint(0, 1)}, check_html=False)
			yield Submission(views.Answers, check_html=False)

		if self.subsession.round_number > 1:
			yield Submission(views.PreviousResults, timeout_happened=True, check_html=False)

		if self.player.inactive < self.session.config['inactive_threshold']:

			yield (views.Preparation)
			if self.participant.id_in_session == 1 | self.participant.id_in_session == 9:
				yield Submission(views.Beliefs_before_PNB, timeout_happened=True, check_html=False)
				yield Submission(views.Beliefs_before_EE, timeout_happened=True, check_html=False)
				yield Submission(views.Beliefs_before_NE, timeout_happened=True, check_html=False)
				yield Submission(views.Contribute_uncond, timeout_happened=True, check_html=False)

			else:
				yield (views.Beliefs_before_PNB, {'personal_normative_beliefs': random.randint(0, Constants.endowment)})
				yield Submission(views.Beliefs_before_EE, {'empirical_expectations0': 2,
													   'empirical_expectations1': 2,
													   'empirical_expectations2': 2,
													   'empirical_expectations3': 2,
													   'empirical_expectations4': 2}, check_html=False)
				yield Submission(views.Beliefs_before_NE, {'normative_expectations0': 2,
													   'normative_expectations1': 2,
													   'normative_expectations2': 2,
													   'normative_expectations3': 2,
													   'normative_expectations4': 2,
													   'normative_expectations5': 2}, check_html=False)

				yield (views.Contribute_uncond, {'contribution': random.randint(0, Constants.endowment)})

			yield Submission(views.WaitNextRound1, timeout_happened=True, check_html=False)
			# yield Submission(views.ResultsWaitPage1, timeout_happened=True, check_html=False)
			yield Submission(views.WaitNextRound2, timeout_happened=True, check_html=False)
			# yield Submission(views.ResultsWaitPage2, timeout_happened=True, check_html=False)
			yield Submission(views.Results, timeout_happened=True, check_html=False)

		elif self.player.inactive >= self.session.config['inactive_threshold']:
			yield Submission(views.Preparation, timeout_happened=True, check_html=False)
			yield Submission(views.Beliefs_before_PNB, timeout_happened=True, check_html=False)
			yield Submission(views.Beliefs_before_EE, timeout_happened=True, check_html=False)
			yield Submission(views.Beliefs_before_NE, timeout_happened=True, check_html=False)
			yield Submission(views.Contribute_uncond, timeout_happened=True, check_html=False)
			yield Submission(views.WaitNextRound1, timeout_happened=True, check_html=False)
			# yield Submission(views.ResultsWaitPage1, timeout_happened=True, check_html=False)
			yield Submission(views.WaitNextRound2, timeout_happened=True, check_html=False)
			yield Submission(views.Results, timeout_happened=True, check_html=False)
