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
        # if any player in group skipped game due to long wait times
        if sum(p.participant.vars.get('go_to_the_end', False) for p in self.get_players()) > 0:
            self.skipped_whole_game = True
        # if all players stayed and got successfully matched
        else:
            self.skipped_whole_game = False
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

    def set_fine_rate(self):
        # get rates the group chose
        chosen_rates = []
        for p in self.get_players():
            chosen_rates.append(p.vote)
        print("chosen_rates =", chosen_rates)
        # which of these rates got 2 or more votes?
        rates_with_two_votes = [k for k, v in dict(Counter(chosen_rates)).items() if v >= 2]
        if not rates_with_two_votes:
            # no rate got at least two votes, pick at random
            fine_rate = random.choice(["0%", "30%", "60%", "80%"])
        elif len(rates_with_two_votes) == 2:
            # two rates got two votes each, randomly choose one
            fine_rate = random.choice(rates_with_two_votes)
        else:
            # if only one rate got two votes
            fine_rate = rates_with_two_votes[0]
        print("fine_rate =", fine_rate)
        self.fine_rate = fine_rate
        # as a decimal
        if fine_rate == "0%":
            fine_rate = 0
        elif fine_rate == "30%":
            fine_rate = 0.3
        elif fine_rate == "60%":
            fine_rate = 0.6
        elif fine_rate == "80%":
            fine_rate = 0.8
        print("fine_rate decimal =", fine_rate)
        # set fine rate
        for p in self.get_players():
            p.participant.vars['part2_finerate'] = fine_rate

    def set_payoffs(self):
        group_account = 0
        for p in self.get_players():
            print('Player', p.id_in_group, 'allocated', p.allocation, 'of', p.participant.vars['part2_endowment'])
            group_account += p.allocation
        self.group_account = group_account
        print('group account =', group_account)
        group_payoff = group_account * 2
        print('group payoff =', group_payoff)
        fine_rate = self.get_player_by_id(1).participant.vars['part2_finerate']
        if fine_rate > 0:
            fixed = c(4)
        else:
            fixed = c(0)
        for p in self.get_players():
            p.fined = (fine_rate * (p.participant.vars['part2_endowment'] - p.allocation)) + fixed
            print('Player', p.id_in_group, 'fined amount =', p.fined)
            p.payoff = (p.participant.vars['part2_endowment'] - p.allocation) + \
                       (group_payoff / Constants.players_per_group) - p.fined
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
    fine_rate = models.StringField()
    group_timeout = models.BooleanField()
    skipped_whole_game = models.BooleanField()


class Player(BasePlayer):
    endowment = models.CurrencyField()
    vote = models.StringField(label="Which fine rate do you vote for in this round?",
                               choices=['0%', '30%', '60%', '80%'])
    allocation = models.CurrencyField(label="How many tokens would you like to allocate to the group account "
                                            "in this round?", min=c(0))
    fined = models.CurrencyField()
    timeoutVote = models.BooleanField()
    timeoutAllocate = models.BooleanField()
    secsSpentWaiting = models.IntegerField()

    def allocation_max(self):
        return self.participant.vars['part2_endowment']
