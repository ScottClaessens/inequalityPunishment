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


class Comprehension(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3']


class Practice1(Page):
    form_model = 'player'
    form_fields = ['practiceAllocation']


class PracticeResults(Page):
    def vars_for_template(self):
        kept = c(50) - self.player.practiceAllocation
        total = c(120) + self.player.practiceAllocation
        earn = kept + (total/2)
        return dict(
            kept=kept,
            total=total,
            back=total/2,
            earn=earn
        )


class StartGame(Page):
    def before_next_page(self):
        self.participant.vars['waitStartTime'] = time.time()


page_sequence = [
    Intro1,
    Intro2,
    Intro3,
    Comprehension,
    Practice1,
    PracticeResults,
    StartGame
]
