from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        if self.round_number == 1:
            yield pages.IntroPart2a
            if self.session.config['treatment'] != 'equality':
                yield pages.IntroPart2b
            yield pages.IntroPart2Phase1a
            yield pages.IntroPart2Phase1b
            yield pages.IntroPart2Phase1c
            yield pages.IntroPart2Phase1d
        if self.round_number == 5:
            yield pages.IntroPart2Phase2a
            yield pages.IntroPart2Phase2b
            yield pages.IntroPart2Phase2c
            yield pages.IntroPart2Phase2d
            yield pages.IntroPart2Phase2e
        if self.round_number == 9:
            yield pages.IntroPart2Phase3
        if self.round_number == 13:
            yield pages.IntroPart2Phase4
        if self.round_number == 17:
            yield pages.IntroPart2Phase5
        if self.round_number == 1:
            if self.session.config['treatment'] == 'skills':
                yield pages.CompPart2Phase1a, dict(comp1a='Type-A',
                                                   comp1b='Type-B',
                                                   comp1c='Type-B',
                                                   comp1d='Type-A',
                                                   comp2=c(80),
                                                   comp3=c(20),
                                                   comp4a=c(80),
                                                   comp4b=c(20),
                                                   comp5a=c(56),
                                                   comp5b=c(50),
                                                   comp5c=c(44))
            elif self.session.config['treatment'] == 'equality':
                yield pages.CompPart2Phase1a, dict(comp6=c(50),
                                                   comp7a=c(50),
                                                   comp7b=c(50),
                                                   comp8a=c(86),
                                                   comp8b=c(71),
                                                   comp8c=c(56))
            else:
                yield pages.CompPart2Phase1a, dict(comp2=c(80),
                                                   comp3=c(20),
                                                   comp4a=c(80),
                                                   comp4b=c(20),
                                                   comp5a=c(56),
                                                   comp5b=c(50),
                                                   comp5c=c(44))
            yield pages.CompPart2Phase1b
        if self.round_number == 5:
            yield pages.CompPart2Phase2a, dict(comp9=80,
                                               comp10=0,
                                               comp11='Private account',
                                               comp12='Yes',
                                               comp13='60%',
                                               comp14=c(4),
                                               comp15a=c(0),
                                               comp15b=c(12))
            yield pages.CompPart2Phase2b
        if self.round_number in [5, 9, 13, 17]:
            yield pages.Vote, dict(vote=random.choice(["0%", "30%", "60%", "80%"]))
            yield pages.VoteResult
        yield pages.Decision, dict(allocation=c(0))
        yield pages.Results
