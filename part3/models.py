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
Part 3
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
    gender = models.StringField(label="What is your gender?", choices=[
        ["Male", "Male"], ["Female", "Female"], ["Other", "Other"]
    ], widget=widgets.RadioSelect, blank=True)
    age = models.IntegerField(label="What is your age?", min=18, max=100, blank=True)
    ethnicity = models.StringField(label="What is your ethnic group?",
                                   choices=[
                                        ["Asian", "Asian or Asian British"],
                                        ["Black", "Black or Black British"],
                                        ["Mixed", "Mixed"],
                                        ["White", "White"],
                                        ["Other", "Other ethnic group"]
                                   ], widget=widgets.RadioSelect, blank=True)
    employed = models.StringField(label="Are you currently employed?", choices=[['No', 'No'], ['Yes', 'Yes']],
                                  widget=widgets.RadioSelect, blank=True)
    married = models.StringField(label="Are you currently married?", choices=[['No', 'No'], ['Yes', 'Yes']],
                                 widget=widgets.RadioSelect, blank=True)
    religious = models.StringField(label="Are you religious?", choices=[['No', 'No'], ['Yes', 'Yes']],
                                   widget=widgets.RadioSelect, blank=True)
    education = models.IntegerField(label="What is the highest level of education you have completed?",
                                    choices=[
                                        [1, "Primary school"],
                                        [2, "GCSEs or equivalent"],
                                        [3, "A-Levels or equivalent"],
                                        [4, "University undergraduate programme"],
                                        [5, "University postgraduate programme"],
                                        [6, "Doctoral degree"]
                                    ], widget=widgets.RadioSelect, blank=True)
    income = models.IntegerField(label="Please estimate your annual household income.",
                                    choices=[
                                        [1, "Below £10,000"],
                                        [2, "£10,001 - £20,000"],
                                        [3, "£20,001 - £30,000"],
                                        [4, "£30,001 - £40,000"],
                                        [5, "£40,001 - £50,000"],
                                        [6, "Above £50,000"]
                                    ], widget=widgets.RadioSelect, blank=True)
    fair = models.IntegerField(label="How fair do you think the distribution of endowments was in your group?",
                               choices=[
                                   [5, 'Extremely fair'],
                                   [4, 'Somewhat fair'],
                                   [3, 'Neither fair nor unfair'],
                                   [2, 'Somewhat unfair'],
                                   [1, 'Extremely unfair']
                               ], widget=widgets.RadioSelectHorizontal)
    manipulation = models.IntegerField(label="How were endowments distributed in your group?",
                                       choices=[
                                           [1, 'Equally'],
                                           [2, 'By performance in Part 1'],
                                           [3, 'By random chance'],
                                           [4, 'By performance in Part 1 with 50% chance and by chance with 50% chance']
                                       ], widget=widgets.RadioSelectHorizontal)
    attention = models.IntegerField(label="If you are reading this question, please answer with 'Strongly agree'",
                                    choices=[
                                        [5, 'Strongly agree'],
                                        [4, 'Agree'],
                                        [3, 'Neither agree nor disagree'],
                                        [2, 'Disagree'],
                                        [1, 'Strongly disagree']
                                    ], widget=widgets.RadioSelectHorizontal)
    sdo1 = models.IntegerField(label="It is okay if some groups have more of a chance in life than others.",
                               choices=[
                                   [5, 'Strongly agree'],
                                   [4, 'Agree'],
                                   [3, 'Neither agree nor disagree'],
                                   [2, 'Disagree'],
                                   [1, 'Strongly disagree']
                               ], widget=widgets.RadioSelectHorizontal)
    sdo2 = models.IntegerField(label="Inferior groups should stay in their place.",
                               choices=[
                                   [5, 'Strongly agree'],
                                   [4, 'Agree'],
                                   [3, 'Neither agree nor disagree'],
                                   [2, 'Disagree'],
                                   [1, 'Strongly disagree']
                               ], widget=widgets.RadioSelectHorizontal)
    sdo3 = models.IntegerField(label="To get ahead in life, it is sometimes okay to step on other groups.",
                               choices=[
                                   [5, 'Strongly agree'],
                                   [4, 'Agree'],
                                   [3, 'Neither agree nor disagree'],
                                   [2, 'Disagree'],
                                   [1, 'Strongly disagree']
                               ], widget=widgets.RadioSelectHorizontal)
    sdo4r = models.IntegerField(label="We should have increased social equality.",
                                choices=[
                                    [5, 'Strongly agree'],
                                    [4, 'Agree'],
                                    [3, 'Neither agree nor disagree'],
                                    [2, 'Disagree'],
                                    [1, 'Strongly disagree']
                                ], widget=widgets.RadioSelectHorizontal)
    sdo5r = models.IntegerField(label="It would be good if groups could be equal.",
                                choices=[
                                    [5, 'Strongly agree'],
                                    [4, 'Agree'],
                                    [3, 'Neither agree nor disagree'],
                                    [2, 'Disagree'],
                                    [1, 'Strongly disagree']
                                ], widget=widgets.RadioSelectHorizontal)
    sdo6r = models.IntegerField(label="We should do what we can to equalise conditions for different groups.",
                                choices=[
                                    [5, 'Strongly agree'],
                                    [4, 'Agree'],
                                    [3, 'Neither agree nor disagree'],
                                    [2, 'Disagree'],
                                    [1, 'Strongly disagree']
                                ], widget=widgets.RadioSelectHorizontal)
    rwa1 = models.IntegerField(
        label="It is always better to trust the judgment of the proper authorities in government "
              "and religion than to listen to the noisy rabble-rousers in our society who are "
              "trying to create doubt in people's minds.",
        choices=[
            [5, 'Strongly agree'],
            [4, 'Agree'],
            [3, 'Neither agree nor disagree'],
            [2, 'Disagree'],
            [1, 'Strongly disagree']
        ], widget=widgets.RadioSelectHorizontal)
    rwa2 = models.IntegerField(
        label="It would be best for everyone if the proper authorities censored magazines so "
              "that people could not get their hands on trashy and disgusting material.",
        choices=[
            [5, 'Strongly agree'],
            [4, 'Agree'],
            [3, 'Neither agree nor disagree'],
            [2, 'Disagree'],
            [1, 'Strongly disagree']
        ], widget=widgets.RadioSelectHorizontal)
    rwa3 = models.IntegerField(
        label="Our country will be destroyed some day if we do not smash the perversions eating "
              "away at our moral fibre and traditional beliefs.",
        choices=[
            [5, 'Strongly agree'],
            [4, 'Agree'],
            [3, 'Neither agree nor disagree'],
            [2, 'Disagree'],
            [1, 'Strongly disagree']
        ], widget=widgets.RadioSelectHorizontal)
    rwa4r = models.IntegerField(
        label="People should pay less attention to The Bible and other traditional forms of "
              "religious guidance, and instead develop their own personal standards of what is "
              "moral and immoral",
        choices=[
            [5, 'Strongly agree'],
            [4, 'Agree'],
            [3, 'Neither agree nor disagree'],
            [2, 'Disagree'],
            [1, 'Strongly disagree']
        ], widget=widgets.RadioSelectHorizontal)
    rwa5r = models.IntegerField(
        label="Atheists and others who have rebelled against established religions are no doubt "
              "every bit as good and virtuous as those who attend church regularly.",
        choices=[
            [5, 'Strongly agree'],
            [4, 'Agree'],
            [3, 'Neither agree nor disagree'],
            [2, 'Disagree'],
            [1, 'Strongly disagree']
        ], widget=widgets.RadioSelectHorizontal)
    rwa6r = models.IntegerField(
        label="Some of the best people in our country are those who are challenging our "
              "government, criticising religion, and ignoring the 'normal way' things are "
              "supposed to be done",
        choices=[
            [5, 'Strongly agree'],
            [4, 'Agree'],
            [3, 'Neither agree nor disagree'],
            [2, 'Disagree'],
            [1, 'Strongly disagree']
        ], widget=widgets.RadioSelectHorizontal)
    meanSDO = models.FloatField()
    meanRWA = models.FloatField()
    feedback = models.LongStringField(label="Please enter any feedback here:", blank=True)
