from . import models
from .models import Constants
from ._builtin import Page
from otree.db.models import BooleanField as m
import otree.forms
import datetime


class Info(Page):

    def get_timeout_seconds(self):
        self.participant.vars['expiry'] = self.session.config['start_datetime'] + datetime.timedelta(
            seconds=self.session.config['seconds_per_round'])
        print("This is EXPIRY ", self.participant.vars['expiry'])
        print("this is TIME now ", datetime.datetime.utcnow())
        print("This is what is DISPLAYED ",
              (self.participant.vars['expiry'] - datetime.datetime.utcnow()).total_seconds())
        return (self.participant.vars['expiry'] - datetime.datetime.utcnow()).total_seconds()

    def is_displayed(self):
        return self.subsession.round_number == 1


class Questions(Page):

    timeout_seconds = 12


    form_model = models.Player
    form_fields = ['selectionYellow', 'selectionBlue']

    def vars_for_template(self):
        return {
            'ball_number': self.subsession.round_number,
        }

    # def clean(self, value, model_instance):
    #    return super(BooleanField, self).clean(value, model_instance)
    # def clean(self, value, model_instance):
    #    if value is None and not self.allow_blank:
    #        raise exceptions.ValidationError(field_required_msg)
    #    return super(BooleanField, self).clean(value, model_instance)

    def error_message(self, values):
        if values['selectionYellow'] == None and values['selectionBlue'] == None:
            # otree-core/otree/db/models.py:    def clean(self, value, model_instance):
            # otree-core/otree/db/models.py:        return super(BooleanField, self).clean(value, model_instance)
            # m.clean(self, value=values, model_instance=self.form_model)
            return "Select at least one box."
        elif values['selectionYellow'] != None and values['selectionBlue'] != None:
            if values['selectionYellow'] + values['selectionBlue'] == 2:

                # m.clean(self, value=values, model_instance=self.form_model)
                self.player.selectionYellow = None
                self.player.selectionBlue = None
                return "Select only one box."

    def before_next_page(self):
        self.player.storePayments()
        if self.timeout_happened:
            self.player.timeout_Questions = 1
            self.player.missed_decisions += 1


#class Final(Page):
#    def is_displayed(self):
#        return self.round_number == 20

#    def vars_for_template(self):
        # global_payoff = self.participant.vars['global_payoff']
        # global_payoff += sum([p.payoff for p in self.player.in_all_rounds()])
#        return {'global_payoff': self.participant.vars['payoffNormCompliance']
                #'total_payoff': self.participant.vars['total_pay']
#                }


page_sequence = [
    Info,
    Questions,
    #Final,
]
