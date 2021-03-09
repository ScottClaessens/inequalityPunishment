from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class GroupingWait(WaitPage):
    def is_displayed(self):
        return self.round_number == 1

    def after_all_players_arrive(self):
        self.group.set_treatment()

    group_by_arrival_time = True
    allow_leaving_after = (60 * 10)
    template_name = 'part2game/GroupWait.html'


class Endowments(Page):
    timeout_seconds = 120

    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars['skippedGame'] is False

    def vars_for_template(self):
        return dict(endowment=self.participant.vars['part2_endowment'],
                    treatment=self.group.in_round(1).treatment)


class DecisionAllocate(Page):
    timeout_seconds = 90

    form_model = 'player'
    form_fields = ['allocation']

    def vars_for_template(self):
        return dict(endowment=self.participant.vars['part2_endowment'],
                    treatment=self.group.in_round(1).treatment)

    def is_displayed(self):
        return self.participant.vars['timeoutGroup'] is False and self.participant.vars['skippedGame'] is False

    def before_next_page(self):
        if self.timeout_happened:
            self.player.allocation = self.participant.vars['part2_endowment']
            self.player.timeoutAllocate = True
        else:
            self.player.timeoutAllocate = False
        if self.player.timeoutAllocate:
            self.participant.vars['timeoutCount'] += 1
        else:
            self.participant.vars['timeoutCount'] = 0


class AllocateWait(WaitPage):
    after_all_players_arrive = 'set_payoffs'

    def is_displayed(self):
        return self.participant.vars['timeoutGroup'] is False and self.participant.vars['skippedGame'] is False

    template_name = 'part2game/Wait.html'


class Results(Page):
    timeout_seconds = 90

    def is_displayed(self):
        return self.participant.vars['timeoutGroup'] is False and self.participant.vars['skippedGame'] is False

    def vars_for_template(self):
        kept = self.participant.vars['part2_endowment'] - self.player.allocation
        back = self.group.group_account / 2
        earn = kept + back
        return dict(
            kept=kept,
            back=back,
            earn=earn
        )


class End(Page):
    def vars_for_template(self):
        part1earn = c(30) * self.participant.vars['part1_correct']
        waitEarn = self.participant.vars['waitEarn']
        part2earn = sum([p.payoff for p in self.player.in_all_rounds()]) - waitEarn
        bonus = part1earn + waitEarn + part2earn
        return dict(
            timeout=self.participant.vars['timeoutGroup'],
            encoded=self.participant.vars['part1_correct'],
            part1earn=part1earn,
            part2earn=part2earn,
            waitEarn=waitEarn.to_real_world_currency(self.session),
            bonus=bonus.to_real_world_currency(self.session),
            total=self.participant.payoff_plus_participation_fee()
        )

    def is_displayed(self):
        return self.round_number == 10 and self.participant.vars['skippedGame'] is False


class Skipped(Page):
    def is_displayed(self):
        return self.round_number == 10 and self.participant.vars['skippedGame'] is True

    def vars_for_template(self):
        part1earn = c(30) * self.participant.vars['part1_correct']
        waitEarn = self.participant.vars['waitEarn']
        bonus = part1earn + waitEarn
        return dict(
            encoded=self.participant.vars['part1_correct'],
            part1earn=part1earn,
            waitEarn=waitEarn.to_real_world_currency(self.session),
            bonus=bonus.to_real_world_currency(self.session),
            total=self.participant.payoff_plus_participation_fee()
        )


page_sequence = [
    GroupingWait,
    Endowments,
    DecisionAllocate,
    AllocateWait,
    Results,
    End,
    Skipped
]
