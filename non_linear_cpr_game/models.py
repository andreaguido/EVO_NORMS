from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, BaseLink,
    Currency as c, currency_range,
)

import random
import datetime

author = 'Andrea Guido'

doc = """
An implementation of a non-linear Common Pool Resource game.
Features:
- Group sizes maximum of 6 because of tables of player contributions, empirical expectations elicitation, and normative expectation elicitation.
    Apart from that group sizes must be even numbers (for instruction legibility minimum is 4 per group) 
- current setup for 35 rounds. Minimum number is 5. Number of rounds/stages must be divisible into whole numbers
"""


class Constants(BaseConstants):
    name_in_url = 'page_no'

    ####PARAMETERS TO BE SPECIFIED####
    #0 = 3 x 1 week of same group and 1 week random group; 1 = 3 weeks random group, 1 week same group; 2 = 4 weeks random matching
    players_per_group = 6
    #Groups are formed dynamically in views.py. this constant is used to form groups there
    num_rounds = 35  # change this to 35 XXX before the XP (min 5 rounds -- since 5-week payment) / must be a mult. of 5
    stages = 5 # 5 weeks of the CPR game
    #stages are the number of discrete sections of the game (e.g. one week each)
    endowment = 30
    # endowment in the game
    belief_correct_pay = 5
    # payment correct beliefs
    p_a = 15
    p_b = 0.083
    timer_text = 'Tiempo restante para completar sus decisiones:' #'Time left to complete your decisions:'
    #Text used in most, but not all, places
    ##################################

    players_per_group_display = players_per_group				#set variable equal to 'players_per_group' when running experiment
    other_players_per_group = players_per_group_display-1

    inactive_threshold = 5
    #Manually set inactive threshold to match that in settings.py. Used only for question_5_text

    #question_1_text = "What are your earnings from the Common account?"
    question_1_text = "¿Cuánto gana de su Cuenta Personal?"#What are your earnings from your Private account?"
    question_2_text = "¿Cuánto gana de su Cuenta Común?"#What are your total earnings from both Private and Common account?"
    # set here the text of the questions

    a1_1 = 0
    a1_2 = 0
    a2_1 = 0
    a2_2 = 2
    a3_1 = 2
    a3_2 = 1
    a4_1 = 0
    a4_2 = 0
    a5 = 1
    # set here the right answers to the questions

    text_Instructions = 'non_linear_cpr_game/text_Instructions.html'
    text_EE = 'non_linear_cpr_game/text_EE.html'
    text_PNB = 'non_linear_cpr_game/text_PNB.html'
    text_NE = 'non_linear_cpr_game/text_NE.html'
    text_Contribute_uncond = 'non_linear_cpr_game/text_Contribute_uncond.html'
    text_Inactive = 'non_linear_cpr_game/text_Inactive.html'

    # XXX
    rounds_picture2 = [2, 10, 18, 26, 34]
    rounds_picture3 = [3, 11, 19, 27, 35]
    rounds_picture4 = [4, 12, 20, 28, 36]
    rounds_picture5 = [5, 13, 21, 29]
    rounds_picture6 = [6, 14, 22, 30]
    rounds_picture7 = [7, 15, 23, 31]
    rounds_picture8 = [8, 16, 24, 32]
    rounds_picture9 = [9, 17, 25, 33]
    #for correct images in Preparation.html


class Subsession(BaseSubsession):

    pass


class Group(BaseGroup):

    total_contribution = models.IntegerField()

##REVISE BELOW: ALL THESE FUNCTIONS MAY BE SUPERFLUOUS
#    def norm_calc(self): ##REVISE##
#        #Summarising personal normative beliefs
#        for p in self.get_players():
#            if p.personal_normative_beliefs < Constants.endowment/2:
#                p.personal_normative_beliefs_categories = 0
#            if p.personal_normative_beliefs == Constants.endowment/2:
#                p.personal_normative_beliefs_categories = 1
#            if p.personal_normative_beliefs > Constants.endowment/2:
#                p.personal_normative_beliefs_categories = 2

#        # Calculating others pnb and others contributions
#        for p in self.get_players():
#            number_other_less_50_pnb = [q for q in self.get_players() if q.personal_normative_beliefs_categories == 0]
#            p.number_other_less_50_pnb = len(number_other_less_50_pnb)
#            if p.personal_normative_beliefs_categories == 0:
#                p.number_other_less_50_pnb -= 1			#excludes ones own personal normative beliefs from the calculation

#            number_other_50_pnb = [q for q in self.get_players() if q.personal_normative_beliefs_categories == 1]
#            p.number_other_50_pnb = len(number_other_50_pnb)
#            if p.personal_normative_beliefs_categories == 1:
#                p.number_other_50_pnb -= 1

#            number_other_more_50_pnb = [q for q in self.get_players() if q.personal_normative_beliefs_categories == 2]
#            p.number_other_more_50_pnb = len(number_other_more_50_pnb)
#            if p.personal_normative_beliefs_categories == 2:
#                p.number_other_more_50_pnb -= 1

#            number_other_less_50_contribution = [q for q in self.get_players() if q.contribution < 50]
#            p.number_other_less_50_contribution = len(number_other_less_50_contribution)
#            if p.contribution < 50:
#                p.number_other_less_50_contribution -= 1

#            number_other_50_contribution = [q for q in self.get_players() if q.contribution == 50]
#            p.number_other_50_contribution = len(number_other_50_contribution)
#            if p.contribution == 50:
#                p.number_other_50_contribution -= 1

#            number_other_more_50_contribution = [q for q in self.get_players() if q.contribution > 50]
#            p.number_other_more_50_contribution = len(number_other_more_50_contribution)
#            if p.contribution > 50:
#                p.number_other_more_50_contribution -= 1

#    def calc_disaster(self): ##DELETE##
#        self.unconditional_disaster_value = random.random()
#        self.unconditional_disaster_value_display = round((self.unconditional_disaster_value*10) + 0.5)

#        self.conditional_disaster_value = random.random()
#        self.conditional_disaster_value_display = round((self.conditional_disaster_value*10) + 0.5)

## END REVISION ##

    # XXX DEFINE PAYOFF FUNCTION
    def set_payoffs(self):
        self.total_contribution = sum([p.contribution for p in self.get_players()])

        #Unconditional payoff calculations
        for p in self.get_players():
            if self.total_contribution > 0:
                p.fraction_contribution = p.contribution / self.total_contribution
            else:
                p.fraction_contribution = 0  # if nobody contributed, you included, you get zero
            p.common_account_earnings = (Constants.p_a * self.total_contribution - Constants.p_b * self.total_contribution * self.total_contribution) * p.fraction_contribution
            p.unconditional_payoff = Constants.endowment - p.contribution + p.common_account_earnings
            #print("This is the player's fraction of contribution ", p.fraction_contribution)
            #print("This is the earning from the common account ", p.common_account_earnings, " and this is the total earning ", p.unconditional_payoff, "of player ", p)

        #Combining unconditional payoffs, conditional payoffs, and belief payoffs, in the relevant periods
        for p in self.get_players():
            if self.round_number == p.paying_round_week1:
                p.payoff = p.unconditional_payoff + p.empirical_expectations_payoff + p.normative_expectations_payoff
                p.participant.vars['contribution_payoff_week1'] = p.unconditional_payoff
                p.participant.vars['expectations_payoff_week1'] = p.empirical_expectations_payoff + p.normative_expectations_payoff
                p.participant.vars['payoff_week1'] = p.payoff
            elif self.round_number == p.paying_round_week2:
                p.payoff = p.unconditional_payoff + p.empirical_expectations_payoff + p.normative_expectations_payoff
                p.participant.vars['contribution_payoff_week2'] = p.unconditional_payoff
                p.participant.vars['expectations_payoff_week2'] = p.empirical_expectations_payoff + p.normative_expectations_payoff
                p.participant.vars['payoff_week2'] = p.payoff
            elif self.round_number == p.paying_round_week3:
                p.payoff = p.unconditional_payoff + p.empirical_expectations_payoff + p.normative_expectations_payoff
                p.participant.vars['contribution_payoff_week3'] = p.unconditional_payoff
                p.participant.vars['expectations_payoff_week3'] = p.empirical_expectations_payoff + p.normative_expectations_payoff
                p.participant.vars['payoff_week3'] = p.payoff
            elif self.round_number == p.paying_round_week4:
                p.payoff = p.unconditional_payoff + p.empirical_expectations_payoff + p.normative_expectations_payoff
                p.participant.vars['contribution_payoff_week4'] = p.unconditional_payoff
                p.participant.vars['expectations_payoff_week4'] = p.empirical_expectations_payoff + p.normative_expectations_payoff
                p.participant.vars['payoff_week4'] = p.payoff
            elif self.round_number == p.paying_round_week5:
                p.payoff = p.unconditional_payoff + p.empirical_expectations_payoff + p.normative_expectations_payoff
                p.participant.vars['contribution_payoff_week5'] = p.unconditional_payoff
                p.participant.vars['expectations_payoff_week5'] = p.empirical_expectations_payoff + p.normative_expectations_payoff
                p.participant.vars['payoff_week5'] = p.payoff
            else:
                p.payoff = 0


class Player(BasePlayer):
    inactive = models.IntegerField()  # check in each round if player is active. it adds up to var. score.

    fraction_contribution = models.FloatField()
    common_account_earnings = models.FloatField()

    timeout_already_happened = models.IntegerField(initial=0)
    timeout_Instructions = models.IntegerField(initial=0)
    timeout_Example = models.IntegerField(initial=0)
    timeout_Control = models.IntegerField(initial=0)
    timeout_Answers = models.IntegerField(initial=0)
    timeout_Preparation = models.IntegerField(initial=0)
    timeout_Beliefs_before_PNB = models.IntegerField(initial=0)
    timeout_Beliefs_before_EE = models.IntegerField(initial=0)
    timeout_Beliefs_before_NE = models.IntegerField(initial=0)
    timeout_Reminder = models.IntegerField(initial=0)
    timeout_Contribute_uncond = models.IntegerField(initial=0)

    score = models.FloatField()
    # this variable defines whether the subject is active or not

    #remove the default values in contribution, contribution_hh-ll, question_1-question_5, empirical_expectations, normative_expectations, and personal_normative_beliefs. The defaults values are there only to help with debugging.
    contribution = models.IntegerField(min=0, max=Constants.endowment)

    other_contribution0 = models.IntegerField(min=0, max=Constants.endowment)
    other_contribution1 = models.IntegerField(min=0, max=Constants.endowment)
    other_contribution2 = models.IntegerField(min=0, max=Constants.endowment)
    other_contribution3 = models.IntegerField(min=0, max=Constants.endowment)
    other_contribution4 = models.IntegerField(min=0, max=Constants.endowment)

    other_inactive0 = models.IntegerField()
    other_inactive1 = models.IntegerField()
    other_inactive2 = models.IntegerField()
    other_inactive3 = models.IntegerField()
    other_inactive4 = models.IntegerField()

    other_timeout_Contribute0 = models.IntegerField()
    other_timeout_Contribute1 = models.IntegerField()
    other_timeout_Contribute2 = models.IntegerField()
    other_timeout_Contribute3 = models.IntegerField()
    other_timeout_Contribute4 = models.IntegerField()

    other_contribution_rank0 = models.IntegerField(initial=0, min=0, max=Constants.endowment)
    other_contribution_rank1 = models.IntegerField(initial=0, min=0, max=Constants.endowment)
    other_contribution_rank2 = models.IntegerField(initial=0, min=0, max=Constants.endowment)
    other_contribution_rank3 = models.IntegerField(initial=0, min=0, max=Constants.endowment)
    other_contribution_rank4 = models.IntegerField(initial=0, min=0, max=Constants.endowment)

    unconditional_payoff = models.FloatField()

    total_payoff = models.CurrencyField()

    paying_round_week1 = models.PositiveIntegerField()
    paying_round_week2 = models.PositiveIntegerField()
    paying_round_week3 = models.PositiveIntegerField()
    paying_round_week4 = models.PositiveIntegerField()
    paying_round_week5 = models.PositiveIntegerField()

    cumulative_payoff = models.PositiveIntegerField()
    #Not sure if the above var is needed. Does not seem to be used elsewhere...

    # questions in the page Control
    question_1_1 = models.PositiveIntegerField(
        choices=[
            [0, "25"],
            [1, "15"],
            [2, "5"],
        ]
    )

    question_1_2 = models.PositiveIntegerField(
        choices=[
            [0, "72.9"],
            [1, "52.2"],
            [2, "31.8"]
        ]
    )

    question_2_1 = models.PositiveIntegerField(
        choices=[
            [0, "25"],
            [1, "15"],
            [2, "5"]
        ]
    )

    question_2_2 = models.PositiveIntegerField(
        choices=[
            [0, "72.9"],
            [1, "52.2"],
            [2, "10.7"]
        ]
    )

    question_3_1 = models.PositiveIntegerField(
        choices=[
            [0, "22"],
            [1, "5"],
            [2, "2"]
        ]
    )

    question_3_2 = models.PositiveIntegerField(
        choices=[
            [0, "6.3"],
            [1, "354.9"],
            [2, "14"]
        ]
    )


    question_4_1 = models.PositiveIntegerField(
        choices=[
            [0, "2"],
            [1, "6"],
            [2, "15"]
        ]
    )

    question_4_2 = models.PositiveIntegerField(
        choices=[
            [0, "6.3"],
            [1, "150.4"],
            [2, "14"]
        ]
    )

    question_5 = models.PositiveIntegerField(
        choices=[
            [0, "Usted podrá continuar participando en el experimento sin ningún problema."],
            [1, "Usted será automática y permanentemente expulsado/a del experimento y, en ese caso, no recibirá ningún pago."]
        ]
    )

    correct_answers = models.PositiveIntegerField(default=0)

    empirical_expectations0 = models.IntegerField(min=0, max=Constants.endowment)
    empirical_expectations1 = models.IntegerField(min=0, max=Constants.endowment)
    empirical_expectations2 = models.IntegerField(min=0, max=Constants.endowment)
    empirical_expectations3 = models.IntegerField(min=0, max=Constants.endowment)
    empirical_expectations4 = models.IntegerField(min=0, max=Constants.endowment)

    personal_normative_beliefs = models.IntegerField(min=0, max=Constants.endowment)
    personal_normative_beliefs_categories = models.IntegerField()

    other_pnb_rank0 = models.IntegerField(initial=0, min=0, max=Constants.endowment)
    other_pnb_rank1 = models.IntegerField(initial=0, min=0, max=Constants.endowment)
    other_pnb_rank2 = models.IntegerField(initial=0, min=0, max=Constants.endowment)
    other_pnb_rank3 = models.IntegerField(initial=0, min=0, max=Constants.endowment)
    other_pnb_rank4 = models.IntegerField(initial=0, min=0, max=Constants.endowment)

    normative_expectations0 = models.IntegerField(min=0, max=Constants.endowment)
    normative_expectations1 = models.IntegerField(min=0, max=Constants.endowment)
    normative_expectations2 = models.IntegerField(min=0, max=Constants.endowment)
    normative_expectations3 = models.IntegerField(min=0, max=Constants.endowment)
    normative_expectations4 = models.IntegerField(min=0, max=Constants.endowment)

    empirical_expectations_payoff = models.IntegerField(default=0)
    normative_expectations_payoff = models.IntegerField(default=0)

    def creating_score(self):
        if self.inactive >= self.session.config['inactive_threshold']:
            self.score = 1
        else:
            self.score = random.random()  #  assign random? Why? because it's between 0/1 1 excluded.

    # function used to check control questions
    def control_calc(self):
        if self.question_1_1 == Constants.a1_1:
            self.correct_answers += 1
        if self.question_1_2 == Constants.a1_2:
            self.correct_answers += 1
        if self.question_2_1 == Constants.a2_1:
            self.correct_answers += 1
        if self.question_2_2 == Constants.a2_2:
            self.correct_answers += 1
        if self.question_3_1 == Constants.a3_1:
            self.correct_answers += 1
        if self.question_3_2 == Constants.a3_2:
            self.correct_answers += 1
        if self.question_4_1 == Constants.a4_1:
            self.correct_answers += 1
        if self.question_4_2 == Constants.a4_2:
            self.correct_answers += 1
        if self.question_5 == Constants.a5:
            self.correct_answers += 1

    # define contributions of inactive players
    def inactive_contribution(self): # take any contribution decision from the whole session
        list = []
        for p in self.get_others_in_subsession():
            if p.timeout_Contribute_uncond == 0 and p.contribution is not None:
                list.append(p.contribution)

        if len(list) == 0:
            self.contribution = 0
        elif len(list) > 0:
            self.contribution = random.choice(list)

    # define pnb of inactive players (one random PNB from the whole session)
    def inactive_pnb(self):
        list = []
        for p in self.get_others_in_subsession():
            if p.timeout_Beliefs_before_PNB == 0 and p.personal_normative_beliefs is not None:
                list.append(p.personal_normative_beliefs)

        if len(list) == 0:
            self.personal_normative_beliefs = 0
        elif len(list) > 0:
            self.personal_normative_beliefs = random.choice(list)

    # retrieve others' contributions to be displayed on Results page
    def other_contributions(self):
        for i in range(Constants.players_per_group-1):
            id = self.get_others_in_group()[i]
            if i == 0:
                self.other_contribution0 = id.contribution
                self.other_inactive0 = id.inactive
                self.other_timeout_Contribute0 = id.timeout_Contribute_uncond
            elif i == 1:
                self.other_contribution1 = id.contribution
                self.other_inactive1 = id.inactive
                self.other_timeout_Contribute1 = id.timeout_Contribute_uncond
            elif i == 2:
                self.other_contribution2 = id.contribution
                self.other_inactive2 = id.inactive
                self.other_timeout_Contribute2 = id.timeout_Contribute_uncond
            elif i == 3:
                self.other_contribution3 = id.contribution
                self.other_inactive3 = id.inactive
                self.other_timeout_Contribute3 = id.timeout_Contribute_uncond
            elif i == 4:
                self.other_contribution4 = id.contribution
                self.other_inactive4 = id.inactive
                self.other_timeout_Contribute4 = id.timeout_Contribute_uncond

    def empirical_expectations(self):
        list = []
        for p in self.get_others_in_group():
            list.append(p.contribution)

        list.sort(reverse=True)
        if Constants.players_per_group >= 2:
            self.other_contribution_rank0 = list[0]
        if Constants.players_per_group >= 3:
            self.other_contribution_rank1 = list[1]
        if Constants.players_per_group >= 4:
            self.other_contribution_rank2 = list[2]
        if Constants.players_per_group >= 5:
            self.other_contribution_rank3 = list[3]
        if Constants.players_per_group == 6:
            self.other_contribution_rank4 = list[4]

        #if self.empirical_expectations0 == None:
        #    self.empirical_expectations0 = Constants.belief_correct_pay

        if self.empirical_expectations1 == None:
            self.empirical_expectations1 = Constants.belief_correct_pay

        if self.empirical_expectations2 == None:
            self.empirical_expectations2 = Constants.belief_correct_pay

        if self.empirical_expectations3 == None:
            self.empirical_expectations3 = Constants.belief_correct_pay

        if self.empirical_expectations4 == None:
            self.empirical_expectations4 = Constants.belief_correct_pay

        if self.timeout_already_happened == 0:
            self.empirical_expectations_payoff = (
                max(0, Constants.belief_correct_pay - (abs(self.other_contribution_rank0-self.empirical_expectations0)))+
                max(0, Constants.belief_correct_pay - (abs(self.other_contribution_rank1-self.empirical_expectations1)))+
                max(0, Constants.belief_correct_pay - (abs(self.other_contribution_rank2-self.empirical_expectations2)))+
                max(0, Constants.belief_correct_pay - (abs(self.other_contribution_rank3-self.empirical_expectations3)))+
                max(0, Constants.belief_correct_pay - (abs(self.other_contribution_rank4-self.empirical_expectations4)))
                )
        elif self.timeout_already_happened == 1:
            self.empirical_expectations_payoff = 0

    def normative_expectations(self):
        list = []
        for p in self.get_others_in_group():
            list.append(p.personal_normative_beliefs)

        list.sort(reverse=True)
        if Constants.players_per_group >= 2:
            self.other_pnb_rank0 = list[0]
        if Constants.players_per_group >= 3:
            self.other_pnb_rank1 = list[1]
        if Constants.players_per_group >= 4:
            self.other_pnb_rank2 = list[2]
        if Constants.players_per_group >= 5:
            self.other_pnb_rank3 = list[3]
        if Constants.players_per_group == 6:
            self.other_pnb_rank4 = list[4]

        #if self.normative_expectations0 == None:
        #	self.normative_expectations0 = Constants.belief_correct_pay

        if self.normative_expectations1 == None:
            self.normative_expectations1 = Constants.belief_correct_pay

        if self.normative_expectations2 == None:
            self.normative_expectations2 = Constants.belief_correct_pay

        if self.normative_expectations3 == None:
            self.normative_expectations3 = Constants.belief_correct_pay

        if self.normative_expectations4 == None:
            self.normative_expectations4 = Constants.belief_correct_pay

        if self.timeout_already_happened == 0:
            self.normative_expectations_payoff = (
                max(0, Constants.belief_correct_pay - (abs(self.other_pnb_rank0-self.normative_expectations0)))+
                max(0, Constants.belief_correct_pay - (abs(self.other_pnb_rank1-self.normative_expectations1)))+
                max(0, Constants.belief_correct_pay - (abs(self.other_pnb_rank2-self.normative_expectations2)))+
                max(0, Constants.belief_correct_pay - (abs(self.other_pnb_rank3-self.normative_expectations3)))+
                max(0, Constants.belief_correct_pay - (abs(self.other_pnb_rank4-self.normative_expectations4)))
                )
        elif self.timeout_already_happened == 1:
            self.normative_expectations_payoff = 0

    # this function defines the rounds that will be considered for payment; stage= week
    def payment_rounds(self):
        if self.round_number == 1:
            self.paying_round_week1 = random.randint(1, Constants.num_rounds/Constants.stages)
            self.participant.vars['paying_round_week1'] = self.paying_round_week1
            self.paying_round_week2 = random.randint(1+Constants.num_rounds/Constants.stages, (Constants.num_rounds/Constants.stages)*2)
            self.participant.vars['paying_round_week2'] = self.paying_round_week2
            self.paying_round_week3 = random.randint(1+(Constants.num_rounds/Constants.stages)*2, (Constants.num_rounds/Constants.stages)*3)
            self.participant.vars['paying_round_week3'] = self.paying_round_week3
            self.paying_round_week4 = random.randint(1+(Constants.num_rounds/Constants.stages)*3, (Constants.num_rounds/Constants.stages)*4)
            self.participant.vars['paying_round_week4'] = self.paying_round_week4
            self.paying_round_week5 = random.randint(1+(Constants.num_rounds/Constants.stages)*4, (Constants.num_rounds/Constants.stages)*5)
            self.participant.vars['paying_round_week5'] = self.paying_round_week5
#            self.paying_round_week6 = random.randint(1+(Constants.num_rounds/Constants.stages)*5, (Constants.num_rounds/Constants.stages)*6)
#            self.participant.vars['paying_round_week6'] = self.paying_round_week6
        else:  # update variables
            self.paying_round_week1 = self.in_round(self.round_number - 1).paying_round_week1
            self.paying_round_week2 = self.in_round(self.round_number - 1).paying_round_week2
            self.paying_round_week3 = self.in_round(self.round_number - 1).paying_round_week3
            self.paying_round_week4 = self.in_round(self.round_number - 1).paying_round_week4
            self.paying_round_week5 = self.in_round(self.round_number - 1).paying_round_week5
#            self.paying_round_week6 = self.in_round(self.round_number - 1).paying_round_week6

    def cumulative_payoff(self):
        if self.round_number == Constants.num_rounds:
            self.participant.vars['final_round_contribution'] = self.contribution
        self.total_payoff = sum([p.payoff for p in self.in_all_rounds()])
        self.participant.vars['game_total_payoff'] = self.total_payoff

class Link(BaseLink):
	pass