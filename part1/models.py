from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range
)

author = 'Scott Claessens'

doc = """
Part 1
"""


class Constants(BaseConstants):
    name_in_url = 'part1'
    players_per_group = 4
    num_rounds = 60
    wage = c(30)

    table = {
        'A': 8,  'B': 12, 'C': 14, 'E': 9,  'F': 6,  'G': 24, 'H': 22, 'I': 7,  'J': 5,  'K': 11, 'L': 3,
        'M': 18, 'N': 1,  'O': 21, 'P': 16, 'Q': 23, 'R': 2,  'S': 13, 'T': 19, 'U': 25, 'V': 4,  'W': 25,
        'X': 17, 'Y': 20, 'Z': 15
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    prolificID = models.StringField(label="Please enter your Prolific ID for payment purposes.")
    takePart = models.BooleanField(label="Do you agree to participate in this study?",
                                   choices=[
                                       [True, 'I agree to take part. Take me to the study.'],
                                       [False, 'I do not agree to take part in this study. Take me back to Prolific.']
                                   ], widget=widgets.RadioSelect)
    input1 = models.IntegerField(min=1, max=26)
    input2 = models.IntegerField(min=1, max=26)
    input3 = models.IntegerField(min=1, max=26)
    totalNumAttempted = models.IntegerField()
    totalNumCorrect = models.IntegerField()

