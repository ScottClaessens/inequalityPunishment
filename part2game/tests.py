from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random

class PlayerBot(Bot):
    def play_round(self):
        if self.round_number == 1:
            yield pages.Endowments
        yield pages.DecisionVote, dict(vote=random.choice(['0%', '30%', '60%', '80%']))
        yield pages.DecisionAllocate, dict(allocation=random.randint(0, self.participant.vars['part2_endowment']))
        yield pages.Results
        if self.round_number == 10:
            yield pages.End
