from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from collections import OrderedDict


class IntroPart2a(Page):
    def is_displayed(self):
        return self.round_number == 1


class IntroPart2b(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return dict(
            treatment=self.session.config['treatment']
        )


class IntroPart2c(Page):
    def is_displayed(self):
        return self.round_number == 1 and self.session.config['treatment'] != 'equality'

    def vars_for_template(self):
        return dict(
            treatment=self.session.config['treatment']
        )


class IntroPart2d(Page):
    def is_displayed(self):
        return self.round_number == 1


class IntroPart2Phase1a(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return dict(
            treatment=self.session.config['treatment']
        )


class IntroPart2Phase1b(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return dict(
            treatment=self.session.config['treatment']
        )


class IntroPart2Phase1c(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return dict(
            treatment=self.session.config['treatment']
        )


class IntroPart2Phase1d(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return dict(
            treatment=self.session.config['treatment']
        )


class IntroPart2Phase2a(Page):
    def is_displayed(self):
        return self.round_number == 6


class IntroPart2Phase2b(Page):
    def is_displayed(self):
        return self.round_number == 6


class IntroPart2Phase2c(Page):
    def is_displayed(self):
        return self.round_number == 6


class IntroPart2Phase2d(Page):
    def is_displayed(self):
        return self.round_number == 6

    def vars_for_template(self):
        return dict(
            treatment=self.session.config['treatment']
        )


class IntroPart2Phase2e(Page):
    def is_displayed(self):
        return self.round_number == 6

    def vars_for_template(self):
        return dict(
            treatment=self.session.config['treatment']
        )


class IntroPart2Phase3(Page):
    def is_displayed(self):
        return self.round_number == 11


class IntroPart2Phase4(Page):
    def is_displayed(self):
        return self.round_number == 16


class IntroPart2Phase5(Page):
    def is_displayed(self):
        return self.round_number == 21


class IntroPart2Phase6(Page):
    def is_displayed(self):
        return self.round_number == 26


class CompPart2Phase1a(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return dict(
            treatment=self.session.config['treatment']
        )

    def get_form_fields(self):
        if self.session.config['treatment'] == 'skills':
            return ['comp1a', 'comp1b', 'comp1c', 'comp1d',
                    'comp2', 'comp3', 'comp4a', 'comp4b', 'comp4c',
                    'comp5a', 'comp5b', 'comp5c']
        elif self.session.config['treatment'] == 'equality':
            return ['comp6', 'comp7a', 'comp7b', 'comp8a', 'comp8b', 'comp8c']
        else:
            return ['comp2', 'comp3', 'comp4a', 'comp4b', 'comp4c',
                    'comp5a', 'comp5b', 'comp5c']


class CompPart2Phase1b(Page):
    def is_displayed(self):
        return self.round_number == 1

    # assign types and endowments
    def before_next_page(self):
        self.group.set_types_endowments()


class CompPart2Phase2a(Page):
    form_model = 'player'
    form_fields = ['comp9', 'comp10', 'comp11', 'comp12',
                   'comp13', 'comp14', 'comp15a', 'comp15b']

    def is_displayed(self):
        return self.round_number == 6

    def vars_for_template(self):
        return dict(
            treatment=self.session.config['treatment']
        )


class CompPart2Phase2b(Page):
    def is_displayed(self):
        return self.round_number == 6


class Wait1(WaitPage):
    def is_displayed(self):
        return self.round_number in [1, 6]


class Vote(Page):
    form_model = 'player'
    form_fields = ['vote']

    def is_displayed(self):
        return self.round_number in [6, 11, 16, 21, 26]

    def vars_for_template(self):
        return dict(
            type=self.participant.vars['part2_type'],
            endowment=self.participant.vars['part2_endowment'],
            phase=(self.round_number // 5) + 1,
            treatment=self.session.config['treatment']
        )


class VoteResult(Page):
    def is_displayed(self):
        return self.round_number in [6, 11, 16, 21, 26]

    def vars_for_template(self):
        return dict(
            phase=(self.round_number // 5) + 1,
            finerate=str(int(self.participant.vars['part2_finerate']*100)) + "%"
        )


class Wait2(WaitPage):
    def is_displayed(self):
        return self.round_number in [6, 11, 16, 21, 26]

    after_all_players_arrive = 'set_fine_rate'


class Decision(Page):
    form_model = 'player'
    form_fields = ['allocation']

    def vars_for_template(self):
        return dict(
            type=self.participant.vars['part2_type'],
            endowment=self.participant.vars['part2_endowment'],
            phase=((self.round_number - 1) // 5) + 1,
            round=((self.round_number - 1) % 5) + 1,
            treatment=self.session.config['treatment']
        )


class Wait3(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    def vars_for_template(self):
        return dict(
            phase=(self.round_number // 5) + 1,
            round=((self.round_number - 1) % 5) + 1
        )


page_sequence = [IntroPart2a,
                 IntroPart2b,
                 IntroPart2c,
                 IntroPart2d,
                 IntroPart2Phase1a,
                 IntroPart2Phase1b,
                 IntroPart2Phase1c,
                 IntroPart2Phase1d,
                 IntroPart2Phase2a,
                 IntroPart2Phase2b,
                 IntroPart2Phase2c,
                 IntroPart2Phase2d,
                 IntroPart2Phase2e,
                 IntroPart2Phase3,
                 IntroPart2Phase4,
                 IntroPart2Phase5,
                 IntroPart2Phase6,
                 CompPart2Phase1a,
                 CompPart2Phase1b,
                 CompPart2Phase2a,
                 CompPart2Phase2b,
                 Wait1,
                 Vote,
                 Wait2,
                 VoteResult,
                 Decision,
                 Wait3,
                 Results]
