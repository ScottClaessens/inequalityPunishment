from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro1(Page):
    pass
    # timeout_seconds = 60


class Intro2(Page):
    pass
    # timeout_seconds = 60


class Intro3(Page):
    pass
    # timeout_seconds = 60


class Intro4(Page):
    pass
    # timeout_seconds = 60


class Intro5(Page):
    pass
    # timeout_seconds = 90


class Comprehension(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4']
    # timeout_seconds = 120


class Practice(Page):
    form_model = 'player'
    form_fields = ['practiceVote', 'practiceAllocation']
    # timeout_seconds = 60


class PracticeResults(Page):
    def vars_for_template(self):
        kept = c(50) - self.player.practiceAllocation
        total = c(120) + self.player.practiceAllocation
        fined = 0.3 * kept
        earn = kept + (total/2) - fined - c(4)
        return dict(
            kept=kept,
            total=total,
            back=total/2,
            fined=fined,
            earn=earn
        )
    # timeout_seconds = 60


class StartGame(Page):
    pass
    # timeout_seconds = 60


page_sequence = [
    Intro1,
    Intro2,
    Intro3,
    Intro4,
    Intro5,
    Comprehension,
    Practice,
    PracticeResults,
    StartGame
]
