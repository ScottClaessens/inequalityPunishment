from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        yield pages.Intro1
        yield pages.Intro2
        yield pages.Intro3
        yield pages.Intro4
        yield pages.Intro5
        yield pages.Comprehension, dict(q1=c(140),
                                        q2=c(280),
                                        q3=c(70),
                                        q4=c(72))
        yield pages.Practice1, dict(practiceVote=random.choice(['0%', '30%', '60%', '80%']))
        yield pages.Practice2, dict(practiceAllocation=random.randint(0, 50))
        yield pages.PracticeResults
        yield pages.StartGame
