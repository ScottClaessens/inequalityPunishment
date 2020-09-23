from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Demographics(Page):
    form_model = 'player'
    form_fields = ['gender', 'age', 'ethnicity', 'employed', 'religious',
                   'married', 'education', 'income', 'fair', 'manipulation']


class Survey(Page):
    form_model = 'player'

    def get_form_fields(self):
        fields = ['sdo1', 'sdo2', 'sdo3', 'sdo4r', 'sdo5r', 'sdo6r',
                  'rwa1', 'rwa2', 'rwa3', 'rwa4r', 'rwa5r', 'rwa6r',
                  'attention']
        random.shuffle(fields)
        return fields

    def before_next_page(self):
        self.player.meanSDO = sum([self.player.sdo1, self.player.sdo2, self.player.sdo3,
                                   6 - self.player.sdo4r, 6 - self.player.sdo5r, 6 - self.player.sdo6r]) / 6
        self.player.meanRWA = sum([self.player.rwa1, self.player.rwa2, self.player.rwa3,
                                   6 - self.player.rwa4r, 6 - self.player.rwa5r, 6 - self.player.rwa6r]) / 6


class Feedback(Page):
    form_model = 'player'
    form_fields = ['feedback']


class End(Page):
    pass


page_sequence = [
    Demographics,
    Survey,
    Feedback,
    End
]
