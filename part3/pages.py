from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Demographics(Page):
    form_model = 'player'
    form_fields = ['gender', 'age', 'ethnicity', 'employed',
                   'married', 'education', 'income', 'fair']


class Survey(Page):
    form_model = 'player'

    def get_form_fields(self):
        fields = ['sdo1', 'sdo2', 'sdo3', 'sdo4', 'sdo5', 'sdo6',
                  'rwa1', 'rwa2', 'rwa3', 'rwa4', 'rwa5', 'rwa6']
        random.shuffle(fields)
        return fields


class End(Page):
    pass


page_sequence = [
    Demographics,
    Survey,
    End
]
