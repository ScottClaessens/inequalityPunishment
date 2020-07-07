from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class GroupingWait(WaitPage):
    def is_displayed(self):
        return self.round_number == 1

    group_by_arrival_time = True
    after_all_players_arrive = 'set_treatment'
    template_name = 'part2game/GroupWait.html'


class Endowments(Page):
    timeout_seconds = 60

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return dict(endowment=self.participant.vars['part2_endowment'])


class DecisionVote(Page):
    timeout_seconds = 45

    form_model = 'player'
    form_fields = ['vote']

    def vars_for_template(self):
        return dict(endowment=self.participant.vars['part2_endowment'])

    def is_displayed(self):
        return self.participant.vars['timeoutGroup'] is False

    def before_next_page(self):
        if self.timeout_happened:
            self.player.vote = '0%'
            self.player.timeoutVote = True
        else:
            self.player.timeoutVote = False


class VoteWait(WaitPage):
    after_all_players_arrive = 'set_fine_rate'

    def is_displayed(self):
        return self.participant.vars['timeoutGroup'] is False


class DecisionAllocate(Page):
    timeout_seconds = 45

    form_model = 'player'
    form_fields = ['allocation']

    def vars_for_template(self):
        return dict(endowment=self.participant.vars['part2_endowment'])

    def is_displayed(self):
        return self.participant.vars['timeoutGroup'] is False

    def before_next_page(self):
        if self.timeout_happened:
            self.player.allocation = self.participant.vars['part2_endowment']
            self.player.timeoutAllocate = True
        else:
            self.player.timeoutAllocate = False
        if self.player.timeoutVote or self.player.timeoutAllocate:
            self.participant.vars['timeoutCount'] += 1
        else:
            self.participant.vars['timeoutCount'] = 0


class AllocateWait(WaitPage):
    after_all_players_arrive = 'set_payoffs'

    def is_displayed(self):
        return self.participant.vars['timeoutGroup'] is False


class Results(Page):
    timeout_seconds = 45

    def is_displayed(self):
        return self.participant.vars['timeoutGroup'] is False

    def vars_for_template(self):
        kept = self.participant.vars['part2_endowment'] - self.player.allocation
        back = self.group.group_account / 2
        fined = kept * self.participant.vars['part2_finerate']
        fixed = c(0) if self.group.fine_rate == '0%' else c(4)
        earn = kept + back - fined - fixed
        return dict(
            kept=kept,
            back=back,
            fined=fined,
            fixed=fixed,
            earn=earn
        )


class End(Page):
    def vars_for_template(self):
        part1earn = c(30) * self.participant.vars['part1_correct']
        part2earn = sum([p.payoff for p in self.player.in_all_rounds()])
        bonus = part1earn + part2earn
        return dict(
            timeout=self.participant.vars['timeoutGroup'],
            encoded=self.participant.vars['part1_correct'],
            part1earn=part1earn,
            part2earn=part2earn,
            bonus=bonus.to_real_world_currency(self.session),
            total=self.participant.payoff_plus_participation_fee()
        )

    def is_displayed(self):
        return self.round_number == 10


page_sequence = [
    GroupingWait,
    Endowments,
    DecisionVote,
    VoteWait,
    DecisionAllocate,
    AllocateWait,
    Results,
    End
]
