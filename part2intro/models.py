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


author = 'Scott Claessens'

doc = """
Part 2 (Intro)
"""


class Constants(BaseConstants):
    name_in_url = 'part2intro'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q1 = models.CurrencyField(label="How many tokens are there in the group account?")
    q2 = models.CurrencyField(label="How many tokens are there in the group account after being doubled?")
    q3 = models.CurrencyField(label="How many tokens will you get back from the group account?")

    practiceAllocation = models.CurrencyField(label="How many tokens would you like to allocate to the group account "
                                                    "in this round?", min=c(0), max=c(50))

    def q1_error_message(self, value):
        if value != c(140):
            return 'The correct answer is 140 tokens: 20 (allocated by you) + 120 (allocated by others)'

    def q2_error_message(self, value):
        if value != c(280):
            return 'The correct answer is 280 tokens: 140 (total allocated to group account) doubled'

    def q3_error_message(self, value):
        if value != c(70):
            return 'The correct answer is 70 tokens: 280 (doubled amount in group account) divided between 4 players'
