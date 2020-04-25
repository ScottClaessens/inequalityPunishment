from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time
import random


class Welcome(Page):
    def is_displayed(self):
        return self.round_number == 1


class IntroPart1(Page):
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        # user has 5 minutes to complete as many pages as possible
        self.participant.vars['part1_expiry'] = time.time() + (5 * 60)
        # set initial letters
        random.seed(0)
        self.participant.vars['part1_letter1'] = random.choice(list(Constants.table.keys()))
        random.seed(1)
        self.participant.vars['part1_letter2'] = random.choice(list(Constants.table.keys()))
        random.seed(2)
        self.participant.vars['part1_letter3'] = random.choice(list(Constants.table.keys()))
        random.seed(3)
        self.participant.vars['part1_letter4'] = random.choice(list(Constants.table.keys()))
        random.seed(4)
        self.participant.vars['part1_letter5'] = random.choice(list(Constants.table.keys()))
        # set correct, incorrect, and earnings
        self.participant.vars['part1_correct'] = 0
        self.participant.vars['part1_incorrect'] = 0
        self.participant.vars['part1_earnings'] = 0


class Task(Page):
    form_model = 'player'
    form_fields = ['input1',
                   'input2',
                   'input3',
                   'input4',
                   'input5']

    def vars_for_template(self):
        return dict(
            letter1=self.participant.vars['part1_letter1'],
            letter2=self.participant.vars['part1_letter2'],
            letter3=self.participant.vars['part1_letter3'],
            letter4=self.participant.vars['part1_letter4'],
            letter5=self.participant.vars['part1_letter5'],
            wage="%.2f" % Constants.wage,
            correct=self.participant.vars['part1_correct'],
            incorrect=self.participant.vars['part1_incorrect'],
            earnings="%.2f" % self.participant.vars['part1_earnings']
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
                self.player.input3 == Constants.table[self.participant.vars['part1_letter3']] and
                self.player.input4 == Constants.table[self.participant.vars['part1_letter4']] and
                self.player.input5 == Constants.table[self.participant.vars['part1_letter5']]
        ):
            self.participant.vars['part1_correct'] += 1
            self.participant.vars['part1_earnings'] += Constants.wage
            self.player.payoff += c(Constants.wage * 1/self.session.config['real_world_currency_per_point'])
        else:
            self.participant.vars['part1_incorrect'] += 1
        # new letters
        random.seed((self.round_number * 5))
        self.participant.vars['part1_letter1'] = random.choice(list(Constants.table.keys()))
        random.seed((self.round_number * 5) + 1)
        self.participant.vars['part1_letter2'] = random.choice(list(Constants.table.keys()))
        random.seed((self.round_number * 5) + 2)
        self.participant.vars['part1_letter3'] = random.choice(list(Constants.table.keys()))
        random.seed((self.round_number * 5) + 3)
        self.participant.vars['part1_letter4'] = random.choice(list(Constants.table.keys()))
        random.seed((self.round_number * 5) + 4)
        self.participant.vars['part1_letter5'] = random.choice(list(Constants.table.keys()))


page_sequence = [Welcome,
                 IntroPart1,
                 Task]
