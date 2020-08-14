from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time
import random


class ProlificID(Page):
    form_model = 'player'
    form_fields = ['prolificID']

    def is_displayed(self):
        return self.round_number == 1


class Welcome(Page):
    form_model = 'player'
    form_fields = ['takePart']

    def is_displayed(self):
        return self.round_number == 1


class ReturnToProlific(Page):
    def is_displayed(self):
        return self.round_number == 1 and self.player.takePart is False


class StudyOverview(Page):
    def is_displayed(self):
        return self.round_number == 1


class IntroPart1(Page):
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        # user has 3 minutes to complete as many pages as possible
        self.participant.vars['part1_expiry'] = time.time() + (3 * 60)
        # set initial letters
        random.seed(0)
        self.participant.vars['part1_letter1'] = random.choice(list(Constants.table.keys()))
        random.seed(1)
        self.participant.vars['part1_letter2'] = random.choice(list(Constants.table.keys()))
        random.seed(2)
        self.participant.vars['part1_letter3'] = random.choice(list(Constants.table.keys()))
        # set correct, incorrect, and earnings
        self.participant.vars['part1_correct'] = 0
        self.participant.vars['part1_incorrect'] = 0
        self.participant.vars['part1_earnings'] = c(0)


class Task(Page):
    form_model = 'player'
    form_fields = ['input1',
                   'input2',
                   'input3']

    def vars_for_template(self):
        return dict(
            letter1=self.participant.vars['part1_letter1'],
            letter2=self.participant.vars['part1_letter2'],
            letter3=self.participant.vars['part1_letter3'],
            wage=Constants.wage,
            correct=self.participant.vars['part1_correct'],
            incorrect=self.participant.vars['part1_incorrect'],
            earnings=self.participant.vars['part1_earnings']
        )

    def get_timeout_seconds(self):
        return self.participant.vars['part1_expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3

    def before_next_page(self):
        # did they get it right?
        if (
                self.player.input1 == Constants.table[self.participant.vars['part1_letter1']] and
                self.player.input2 == Constants.table[self.participant.vars['part1_letter2']] and
                self.player.input3 == Constants.table[self.participant.vars['part1_letter3']]
        ):
            self.participant.vars['part1_correct'] += 1
            self.participant.vars['part1_earnings'] += Constants.wage
            self.player.payoff += Constants.wage
        else:
            self.participant.vars['part1_incorrect'] += 1
        # new letters
        random.seed((self.round_number * 5))
        self.participant.vars['part1_letter1'] = random.choice(list(Constants.table.keys()))
        random.seed((self.round_number * 5) + 1)
        self.participant.vars['part1_letter2'] = random.choice(list(Constants.table.keys()))
        random.seed((self.round_number * 5) + 2)
        self.participant.vars['part1_letter3'] = random.choice(list(Constants.table.keys()))
        # record vars once timed out
        if self.timeout_happened or self.round_number == Constants.num_rounds:
            self.player.in_round(Constants.num_rounds).totalNumAttempted = \
                self.participant.vars['part1_correct'] + \
                self.participant.vars['part1_incorrect']
            self.player.in_round(Constants.num_rounds).totalNumCorrect = self.participant.vars['part1_correct']


page_sequence = [ProlificID,
                 Welcome,
                 ReturnToProlific,
                 StudyOverview,
                 IntroPart1,
                 Task]
