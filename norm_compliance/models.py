from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    #BaseLink,
    Currency as c, currency_range
)
from otree.db.models import BooleanField as m

author = 'Pablo Lozano'
doc = """
Compliance to a certain norm experiment.
"""


class Constants(BaseConstants):
    name_in_url = 'questions2'
    players_per_group = None
    num_rounds = 20


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # timeout for decision page
    timeout_Questions = models.IntegerField()

    # Modelos para guardar las participant vars
    payoff_norm = models.FloatField()
    #payoff_total = models.FloatField()
    selectionYellow = models.PositiveIntegerField(blank=True, default=None, choices=[
        [1, '']], widget=widgets.RadioSelect, verbose_name="")
    selectionBlue = models.PositiveIntegerField(blank=True, default=None, choices=[
        [1, '']], widget=widgets.RadioSelect, verbose_name="")

    def storePayments(self):
        self.payoff_norm = sum([0.5 for p in self.in_all_rounds(
        ) if p.selectionYellow == 1]) + sum([1 for p in self.in_all_rounds() if p.selectionBlue == 1])
        self.participant.vars['payoffNormCompliance'] = self.payoff_norm
        print("PRINT PAYOFF NORM COMPLIANCE ", self.participant.vars['payoffNormCompliance'])

#    def total_payment(self):
#        self.participant.vars['total_pay'] = self.participant.vars['global_payoff'] + \
#            self.participant.vars['payoffNormCompliance']
#        self.payoff_total = self.participant.vars['total_pay']

    # def clean(self):
    #    m.clean(self, value=self.selectionYellow,
    #            model_instance=self.selectionYellow)
    # otree-core/otree/db/models.py:    def clean(self, value, model_instance):
    # otree-core/otree/db/models.py:        return super(BooleanField, self).clean(value, model_instance)


#class Link(BaseLink):
     #class Link():
#    pass
