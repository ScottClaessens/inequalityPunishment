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


author = 'Scott Claessens'

doc = """
Inequality and punishment (Part 3)
"""


class Constants(BaseConstants):
    name_in_url = 'part3'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender = models.IntegerField(label="What is your gender?", choices=[[1, 'Male'], [2, 'Female'], [3, 'Other']],
                                 widget=widgets.RadioSelect, blank=True)
    age = models.IntegerField(label="What is your age?", min=18, max=100, blank=True)
    ethnicity = models.StringField(label="What is your ethnicity?", blank=True)
    nationality = models.StringField(label="What is your nationality?", blank=True)
    employment = models.IntegerField(label="Are you currently employed?", choices=[[0, 'No'], [1, 'Yes']],
                                     widget=widgets.RadioSelect, blank=True)
    married = models.IntegerField(label="Are you currently married?", choices=[[0, 'No'], [1, 'Yes']],
                                  widget=widgets.RadioSelect, blank=True)
    education = models.StringField(label="What is your highest achieved level of education?",
                                   blank=True)
    income = models.StringField(label="Please estimate your annual household income.", blank=True)

    fair = models.IntegerField(label="How fair do you think the distribution of endowments was in your group?",
                               choices=[
                                   [5, 'Extremely fair'],
                                   [4, 'Somewhat fair'],
                                   [3, 'Neither fair nor unfair'],
                                   [2, 'Somewhat unfair'],
                                   [1, 'Extremely unfair']
                               ], widget=widgets.RadioSelectHorizontal,
                               blank=True)

    sdo1 = models.IntegerField(label="It is okay if some groups have more of a chance in life than others.",
                               choices=[
        [5, 'Strongly agree'],
        [4, 'Agree'],
        [3, 'Neither agree nor disagree'],
        [2, 'Disagree'],
        [1, 'Strongly disagree']
    ], widget=widgets.RadioSelectHorizontal, blank=True)
    sdo2 = models.IntegerField(label="Inferior groups should stay in their place.",
                               choices=[
        [5, 'Strongly agree'],
        [4, 'Agree'],
        [3, 'Neither agree nor disagree'],
        [2, 'Disagree'],
        [1, 'Strongly disagree']
    ], widget=widgets.RadioSelectHorizontal, blank=True)
    sdo3 = models.IntegerField(label="To get ahead in life, it is sometimes okay to step on other groups.",
                               choices=[
        [5, 'Strongly agree'],
        [4, 'Agree'],
        [3, 'Neither agree nor disagree'],
        [2, 'Disagree'],
        [1, 'Strongly disagree']
    ], widget=widgets.RadioSelectHorizontal, blank=True)
    sdo4 = models.IntegerField(label="We should have increased social equality.",
                               choices=[
        [5, 'Strongly agree'],
        [4, 'Agree'],
        [3, 'Neither agree nor disagree'],
        [2, 'Disagree'],
        [1, 'Strongly disagree']
    ], widget=widgets.RadioSelectHorizontal, blank=True)
    sdo5 = models.IntegerField(label="It would be good if groups could be equal.",
                               choices=[
        [5, 'Strongly agree'],
        [4, 'Agree'],
        [3, 'Neither agree nor disagree'],
        [2, 'Disagree'],
        [1, 'Strongly disagree']
    ], widget=widgets.RadioSelectHorizontal, blank=True)
    sdo6 = models.IntegerField(label="We should do what we can to equalise conditions for different groups.",
                               choices=[
        [5, 'Strongly agree'],
        [4, 'Agree'],
        [3, 'Neither agree nor disagree'],
        [2, 'Disagree'],
        [1, 'Strongly disagree']
    ], widget=widgets.RadioSelectHorizontal, blank=True)
    rwa1 = models.IntegerField(label="It is always better to trust the judgment of the proper authorities in government "
                                     "and religion than to listen to the noisy rabble-rousers in our society who are "
                                     "trying to create doubt in people's minds.",
                               choices=[
        [5, 'Strongly agree'],
        [4, 'Agree'],
        [3, 'Neither agree nor disagree'],
        [2, 'Disagree'],
        [1, 'Strongly disagree']
    ], widget=widgets.RadioSelectHorizontal, blank=True)
    rwa2 = models.IntegerField(label="It would be best for everyone if the proper authorities censored magazines so "
                                     "that people could not get their hands on trashy and disgusting material.",
                               choices=[
        [5, 'Strongly agree'],
        [4, 'Agree'],
        [3, 'Neither agree nor disagree'],
        [2, 'Disagree'],
        [1, 'Strongly disagree']
    ], widget=widgets.RadioSelectHorizontal, blank=True)
    rwa3 = models.IntegerField(label="Our country will be destroyed some day if we do not smash the perversions eating "
                                     "away at our moral fibre and traditional beliefs.",
                               choices=[
        [5, 'Strongly agree'],
        [4, 'Agree'],
        [3, 'Neither agree nor disagree'],
        [2, 'Disagree'],
        [1, 'Strongly disagree']
    ], widget=widgets.RadioSelectHorizontal, blank=True)
    rwa4 = models.IntegerField(label="People should pay less attention to The Bible and other traditional forms of "
                                     "religious guidance, and instead develop their own personal standards of what is "
                                     "moral and immoral",
                               choices=[
        [5, 'Strongly agree'],
        [4, 'Agree'],
        [3, 'Neither agree nor disagree'],
        [2, 'Disagree'],
        [1, 'Strongly disagree']
    ], widget=widgets.RadioSelectHorizontal, blank=True)
    rwa5 = models.IntegerField(label="Atheists and others who have rebelled against established religions are no doubt "
                                     "every bit as good and virtuous as those who attend church regularly.",
                               choices=[
        [5, 'Strongly agree'],
        [4, 'Agree'],
        [3, 'Neither agree nor disagree'],
        [2, 'Disagree'],
        [1, 'Strongly disagree']
    ], widget=widgets.RadioSelectHorizontal, blank=True)
    rwa6 = models.IntegerField(label="Some of the best people in our country are those who are challenging our "
                                     "government, criticising religion, and ignoring the 'normal way' things are "
                                     "supposed to be done",
                               choices=[
        [5, 'Strongly agree'],
        [4, 'Agree'],
        [3, 'Neither agree nor disagree'],
        [2, 'Disagree'],
        [1, 'Strongly disagree']
    ], widget=widgets.RadioSelectHorizontal, blank=True)
