from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random
import time
from collections import Counter

author = 'Scott Claessens'

doc = """
Part 2 (Game)
"""


class Constants(BaseConstants):
    name_in_url = 'part2game'
    players_per_group = 4
    num_rounds = 10


class Subsession(BaseSubsession):
    def creating_session(self):
        self.session.vars['numGroupsFormed'] = 0
        for p in self.get_players():
            p.participant.vars['timeoutGroup'] = False

    def group_by_arrival_time_method(self, waiting_players):
        if len(waiting_players) >= 4:
            for p in waiting_players[:4]:
                p.participant.vars['skippedGame'] = False
                p.skippedGame = False
            print("successfully formed group...")
            return waiting_players[:4]
        for p in waiting_players:
            if p.waiting_too_long():
                # return single player group because player waited too long
                p.participant.vars['skippedGame'] = True
                p.skippedGame = True
                print("player waited too long and skipped game...")
                return [p]


class Group(BaseGroup):
    def set_endowments(self):
        # get scores
        part1 = []
        for p in self.get_players():
            part1.append((p, p.participant.vars['part1_correct']))
        # sort
        part1.sort(key=lambda x: x[1])

        def skill():
            part1[3][0].participant.vars['part2_endowment'] = c(80)
            part1[2][0].participant.vars['part2_endowment'] = c(80)
            part1[1][0].participant.vars['part2_endowment'] = c(20)
            part1[0][0].participant.vars['part2_endowment'] = c(20)

        def luck():
            x = [1, 2, 3, 4]
            random.shuffle(x)
            self.get_player_by_id(x[0]).participant.vars['part2_endowment'] = c(80)
            self.get_player_by_id(x[1]).participant.vars['part2_endowment'] = c(80)
            self.get_player_by_id(x[2]).participant.vars['part2_endowment'] = c(20)
            self.get_player_by_id(x[3]).participant.vars['part2_endowment'] = c(20)
        # get endowments based on treatment
        if self.treatment == 'skill':
            skill()
        elif self.treatment == 'luck':
            luck()
        elif self.treatment == 'uncertain':
            if random.choice([0, 1]) == 0:
                skill()
            else:
                luck()
        elif self.treatment == 'equality':
            for p in self.get_players():
                p.participant.vars['part2_endowment'] = c(50)
        # record endowment
        for p in self.get_players():
            p.endowment = p.participant.vars["part2_endowment"]

    def set_treatment(self):
        # record time spent waiting
        for p in self.get_players():
            t = int(time.time() - p.participant.vars['waitStartTime'])
            if t > 600:
                t = 600
            p.participant.vars["secsSpentWaiting"] = t
            p.secsSpentWaiting = t
            p.participant.vars["waitEarn"] = c((p.participant.vars["secsSpentWaiting"] / 60) *  # num of seconds *
                          (0.05 / self.session.config['real_world_currency_per_point']))        # £0.05 = 12.5 tokens
            p.payoff += p.participant.vars["waitEarn"]
        # if all players stayed and got successfully matched
        sum_skipped = 0
        for p in self.get_players():
            sum_skipped += p.participant.vars['skippedGame']
        if sum_skipped == 0:
            # increase number of groups formed by one
            self.session.vars['numGroupsFormed'] += 1
            # set treatment
            if self.session.config['treatment'] == 'random':
                treatment = ['equality', 'skill', 'luck', 'uncertain'][self.session.vars['numGroupsFormed'] % 4]
            else:
                treatment = self.session.config['treatment']
            self.treatment = treatment
            print('treatment =', treatment)
            # set endowments from treatment
            self.set_endowments()
            # set timeout counter and group timeout
            for p in self.get_players():
                p.participant.vars['timeoutCount'] = 0
                p.participant.vars['timeoutGroup'] = False

    def set_payoffs(self):
        group_account = 0
        for p in self.get_players():
            print('Player', p.id_in_group, 'allocated', p.allocation, 'of', p.participant.vars['part2_endowment'])
            group_account += p.allocation
        self.group_account = group_account
        print('group account =', group_account)
        group_payoff = group_account * 2
        print('group payoff =', group_payoff)
        for p in self.get_players():
            p.payoff = (p.participant.vars['part2_endowment'] - p.allocation) + \
                       (group_payoff / Constants.players_per_group)
            print('Player', p.id_in_group, 'payoff =', p.payoff)
        # and find out if any group members have timed out two rounds in a row
        n = 0
        for p in self.get_players():
            n += (p.participant.vars['timeoutCount'] == 2)
        if n > 0:
            for p in self.get_players():
                p.participant.vars['timeoutGroup'] = True
                self.group_timeout = True

    treatment = models.StringField()
    group_account = models.CurrencyField()
    group_timeout = models.BooleanField()


class Player(BasePlayer):
    endowment = models.CurrencyField()
    allocation = models.CurrencyField(label="How many tokens would you like to allocate to the group account "
                                            "in this round?", min=c(0))
    timeoutAllocate = models.BooleanField()
    secsSpentWaiting = models.IntegerField()
    skippedGame = models.BooleanField()

    def allocation_max(self):
        return self.participant.vars['part2_endowment']

    def waiting_too_long(self):
        return time.time() - self.participant.vars["waitStartTime"] > 10*60
