from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        if self.round_number == 1:
            yield pages.Welcome, dict(takePart=True)
            yield pages.StudyOverview
            yield pages.IntroPart1
        yield pages.Task, dict(input1=random.choice(list(range(1, 27))),
                               input2=random.choice(list(range(1, 27))),
                               input3=random.choice(list(range(1, 27))))
