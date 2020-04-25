from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random
from collections import Counter


author = 'Scott Claessens'

doc = """
Inequality and punishment (Part 2)
"""


class Constants(BaseConstants):
    name_in_url = 'part2'
    players_per_group = 4
    num_rounds = 30


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def set_types_endowments(self):
        # get scores
        part1 = []
        for p in self.get_players():
            part1.append((p, p.participant.vars['part1_correct']))
        # sort
        part1.sort(key=lambda x: x[1])

        def skill():
            part1[3][0].participant.vars['part2_type'] = 'Type A'
            part1[2][0].participant.vars['part2_type'] = 'Type A'
            part1[1][0].participant.vars['part2_type'] = 'Type B'
            part1[0][0].participant.vars['part2_type'] = 'Type B'

        def luck():
            x = [1, 2, 3, 4]
            random.shuffle(x)
            self.get_player_by_id(x[0]).participant.vars['part2_type'] = 'Type A'
            self.get_player_by_id(x[1]).participant.vars['part2_type'] = 'Type A'
            self.get_player_by_id(x[2]).participant.vars['part2_type'] = 'Type B'
            self.get_player_by_id(x[3]).participant.vars['part2_type'] = 'Type B'

        # types
        if self.session.config['treatment'] == 'skills':
            skill()
        elif self.session.config['treatment'] == 'luck':
            luck()
        elif self.session.config['treatment'] == 'uncertain':
            if random.choice([0, 1]) == 0:
                skill()
            else:
                luck()
        elif self.session.config['treatment'] == 'equality':
            for p in self.get_players():
                p.participant.vars['part2_type'] = None
        # endowments
        for p in self.get_players():
            if self.session.config['treatment'] != 'equality':
                if p.participant.vars['part2_type'] == 'Type A':
                    p.participant.vars['part2_endowment'] = c(80)
                else:
                    p.participant.vars['part2_endowment'] = c(20)
            else:
                p.participant.vars['part2_endowment'] = c(50)

    def set_payoffs(self):
        group_account = 0
        for p in self.get_players():
            group_account += p.allocation
        self.group_account = group_account
        group_payoff = group_account*1.6
        if 6 <= self.round_number <= 30:
            fine_rate = self.get_player_by_id(1).participant.vars['part2_finerate']
            if fine_rate > 0:
                fixed = c(4)
            else:
                fixed = c(0)
        else:
            fine_rate = 0
            fixed = c(0)
        for p in self.get_players():
            p.fined = (fine_rate * (p.participant.vars['part2_endowment'] - p.allocation)) + fixed
            p.payoff = (p.participant.vars['part2_endowment'] - p.allocation) + \
                       (group_payoff / Constants.players_per_group) - p.fined

    def set_fine_rate(self):
        # get rates the group chose
        chosen_rates = []
        for p in self.get_players():
            chosen_rates.append(p.vote)
        # which of these rates got 2 or more votes?
        rates_with_two_votes = [k for k, v in dict(Counter(chosen_rates)).items() if v >= 2]
        if not rates_with_two_votes:
            # no rate got at least two votes, pick at random
            fine_rate = random.choice(["0%", "30%", "60%", "80%"])
        elif len(rates_with_two_votes) == 2:
            # two rates got two votes each, randomly choose one
            fine_rate = random.choice(rates_with_two_votes)
        else:
            # if only one rate got two votes
            fine_rate = rates_with_two_votes
        # as a decimal
        if fine_rate[0] == "0%":
            fine_rate = 0
        elif fine_rate[0] == "30%":
            fine_rate = 0.3
        elif fine_rate[0] == "60%":
            fine_rate = 0.6
        elif fine_rate[0] == "80%":
            fine_rate = 0.8
        # set fine rate
        for p in self.get_players():
            p.participant.vars['part2_finerate'] = fine_rate

    group_account = models.CurrencyField()


class Player(BasePlayer):
    # comprehension questions for phase 1
    comp1a = models.StringField(
        label="Member 1:",
        choices=[
            ['Type A', 'Type A'],
            ['Type B', 'Type B']
        ]
    )
    comp1b = models.StringField(
        label="Member 2:",
        choices=[
            ['Type A', 'Type A'],
            ['Type B', 'Type B']
        ]
    )
    comp1c = models.StringField(
        label="Member 3:",
        choices=[
            ['Type A', 'Type A'],
            ['Type B', 'Type B']
        ]
    )
    comp1d = models.StringField(
        label="Member 4:",
        choices=[
            ['Type A', 'Type A'],
            ['Type B', 'Type B']
        ]
    )
    comp2 = models.CurrencyField(label="")
    comp3 = models.CurrencyField(label="")
    comp4a = models.CurrencyField(label="How much do you earn?")
    comp4b = models.CurrencyField(label="How much does the other Type A group member earn?")
    comp4c = models.CurrencyField(label="How much does each Type B group member earn?")
    comp5a = models.CurrencyField(label="How much do you earn if you allocate 0 tokens to the group account?")
    comp5b = models.CurrencyField(label="How much do you earn if you allocate 10 tokens to the group account?")
    comp5c = models.CurrencyField(label="How much do you earn if you allocate 20 tokens to the group account?")
    # in equality treatment
    comp6 = models.CurrencyField(label="How many tokens are each group member endowed with in each round?")
    comp7a = models.CurrencyField(label="How much do you earn?")
    comp7b = models.CurrencyField(label="How much do each of the other group members earn?")
    comp8a = models.CurrencyField(label="How much do you earn if you allocate 0 tokens to the group account?")
    comp8b = models.CurrencyField(label="How much do you earn if you allocate 25 tokens to the group account?")
    comp8c = models.CurrencyField(label="How much do you earn if you allocate 50 tokens to the group account?")

    # comprehension questions for phase 2
    comp9 = models.IntegerField(label="What is the highest possible fine rate (in % form)?")
    comp10 = models.IntegerField(label="What is the lowest possible fine rate (in % form)?")
    comp11 = models.StringField(
        label="Are tokens allocated to the private account or the group account fined?",
        choices=[
            ["Private account", "Private account"],
            ["Group account", "Group account"]
        ]
    )
    comp12 = models.StringField(
        label="Will the voted fine rate be implemented in each of the 5 rounds in Phase 2?",
        choices=[
            ["Yes", "Yes"],
            ["No", "No"]
        ]
    )
    comp13 = models.StringField(
        label="Suppose the votes in your group are: 60%, 80%, 30%, and 60%. What fine rate will be implemented in Phase 2?",
        choices=[
            ["0%", "0%"],
            ["30%", "30%"],
            ["60%", "60%"],
            ["80%", "80%"]
        ]
    )
    comp14 = models.CurrencyField(
        label="If a fine rate greater than 0% is implemented, what is the fixed fine fee that every group member will pay every round in Phase 2?"
    )
    comp15a = models.CurrencyField(
        label="What is your fine payment if the fine rate is voted to be 0%?"
    )
    comp15b = models.CurrencyField(
        label="In addition to the fixed fine fee, what is your fine payment if the fine rate is voted to be 60%?"
    )

    # vote
    vote = models.StringField(
        label="Which fine rate will you vote for in this phase?",
        choices=[
            ["0%", "0%"],
            ["30%", "30%"],
            ["60%", "60%"],
            ["80%", "80%"]
        ]
    )

    # allocation decision
    allocation = models.CurrencyField(
        min=0,
        label="How many tokens will you allocate to the group account in this round?"
    )

    def allocation_max(self):
        return self.participant.vars['part2_endowment']

    # how much fined
    fined = models.CurrencyField()

    # comprehension error messages
    def comp1a_error_message(self, value):
        if value != 'Type A':
            return 'The correct answer is Type A'

    def comp1b_error_message(self, value):
        if value != 'Type B':
            return 'The correct answer is Type B'

    def comp1c_error_message(self, value):
        if value != 'Type B':
            return 'The correct answer is Type B'

    def comp1d_error_message(self, value):
        if value != 'Type A':
            return 'The correct answer is Type A'

    def comp2_error_message(self, value):
        if value != c(80):
            return 'The correct answer is 80 tokens'

    def comp3_error_message(self, value):
        if value != c(20):
            return 'The correct answer is 20 tokens'

    def comp4a_error_message(self, value):
        if value != c(80):
            return 'The correct answer is 80 tokens'

    def comp4b_error_message(self, value):
        if value != c(80):
            return 'The correct answer is 80 tokens'

    def comp4c_error_message(self, value):
        if value != c(20):
            return 'The correct answer is 20 tokens'

    def comp5a_error_message(self, value):
        if value != c(56):
            return 'The correct answer is 56 tokens'

    def comp5b_error_message(self, value):
        if value != c(50):
            return 'The correct answer is 50 tokens'

    def comp5c_error_message(self, value):
        if value != c(44):
            return 'The correct answer is 44 tokens'

    def comp6_error_message(self, value):
        if value != c(50):
            return 'The correct answer is 50 tokens'

    def comp7a_error_message(self, value):
        if value != c(50):
            return 'The correct answer is 50 tokens'

    def comp7b_error_message(self, value):
        if value != c(50):
            return 'The correct answer is 50 tokens'

    def comp8a_error_message(self, value):
        if value != c(86):
            return 'The correct answer is 86 tokens'

    def comp8b_error_message(self, value):
        if value != c(71):
            return 'The correct answer is 71 tokens'

    def comp8c_error_message(self, value):
        if value != c(56):
            return 'The correct answer is 56 tokens'

    def comp9_error_message(self, value):
        if value != 80:
            return 'The correct answer is 80%'

    def comp10_error_message(self, value):
        if value != 0:
            return 'The correct answer 0%'

    def comp11_error_message(self, value):
        if value != 'Private account':
            return 'The correct answer is the private account'

    def comp12_error_message(self, value):
        if value != 'Yes':
            return 'The correct answer is Yes'

    def comp13_error_message(self, value):
        if value != '60%':
            return 'The correct answer is 60%'

    def comp14_error_message(self, value):
        if value != c(4):
            return 'The correct answer is 4 tokens'

    def comp15a_error_message(self, value):
        if value != c(0):
            return 'The correct answer is 0 tokens'

    def comp15b_error_message(self, value):
        if value != c(12):
            return 'The correct answer is 12 tokens'
