from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants

import random

class PlayerBot(Bot):

    def play_round(self):
        yield (views.IntroClimateExperiment)
        yield (views.MyPage, {
        	'q1': random.randint(1, 5),
        	'q2': random.randint(1, 5),
        	'q3': random.randint(1, 5),
        	'q4': random.randint(1, 5),
        	'q5': random.randint(1, 5),
        	'q6': random.randint(1, 5),
        	'q7': random.randint(1, 5),
        	'q8': random.randint(1, 5),
        	'q9': random.randint(1, 5),
        	'q10': random.randint(1, 5),
        	'q11': random.randint(1, 5),
        	'q12': random.randint(1, 5),
        	'q13': random.randint(1, 5),
        	'q14': random.randint(1, 5),
        	'q15': random.randint(1, 5),
        	'q16': random.randint(1, 5),
        	'q17': random.randint(1, 5),
        	'q18': random.randint(1, 5),
        	'q19': random.randint(1, 5),
        	'q20': random.randint(1, 5),
        	'q21': random.randint(1, 5),
        	'q22': random.randint(1, 5),
        	'q23': random.randint(1, 5),
        	'q24': random.randint(1, 5),
        	'q25': random.randint(1, 5),
        	'q26': random.randint(1, 5),
        	'q27': random.randint(1, 5),
        	'q28': random.randint(1, 5),
        	'q29': random.randint(1, 5),
        	'q30': random.randint(1, 5),
        	'q31': random.randint(1, 5),
        	'q32': random.randint(1, 5),
        	'q33': random.randint(1, 5),
        	'q34': random.randint(1, 5),
        	'q35': random.randint(1, 5),
        	'q36': random.randint(1, 5),
        	'q37': random.randint(1, 5),
        	'q38': random.randint(1, 5),
        	'q39': random.randint(1, 5),
        	'q40': random.randint(1, 5),
        	'q41': random.randint(1, 5),
        	'q42': random.randint(1, 5),
        	'q43': random.randint(1, 5),
        	'q44': random.randint(1, 5),
        	})
