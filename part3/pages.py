from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Survey(Page):
    form_model = 'player'
    form_fields = ['gender', 'age', 'ethnicity', 'nationality', 'employment', 'married', 'education',
                   'income', 'fair', 'sdo1', 'sdo2', 'sdo3', 'sdo4', 'sdo5', 'sdo6', 'rwa1', 'rwa2',
                   'rwa3', 'rwa4', 'rwa5', 'rwa6']


class End(Page):
    pass


page_sequence = [
    Survey,
    End
]
