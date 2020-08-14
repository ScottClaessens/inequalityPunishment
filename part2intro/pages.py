from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time


class Intro1(Page):
    pass


class Intro2(Page):
    pass


class Intro3(Page):
    pass


class Intro4(Page):
    pass


class Intro5(Page):
    pass


class Comprehension(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4']


class Practice1(Page):
    form_model = 'player'
    form_fields = ['practiceVote']


class Practice2(Page):
    form_model = 'player'
    form_fields = ['practiceAllocation']


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


class StartGame(Page):
    def before_next_page(self):
        self.participant.vars['waitStartTime'] = time.time()


page_sequence = [
    Intro1,
    Intro2,
    Intro3,
    Intro4,
    Intro5,
    Comprehension,
    Practice1,
    Practice2,
    PracticeResults,
    StartGame
]
