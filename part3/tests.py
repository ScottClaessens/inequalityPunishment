from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
from otree.api import Submission


class PlayerBot(Bot):
    def play_round(self):
        yield pages.Survey, dict(
            gender=1,
            age=26,
            ethnicity='White',
            nationality='British',
            employment=1,
            married=1,
            education='PhD',
            income='$50,000',
            fair=3,
            sdo1=3,
            sdo2=3,
            sdo3=3,
            sdo4=3,
            sdo5=3,
            sdo6=3,
            rwa1=3,
            rwa2=3,
            rwa3=3,
            rwa4=3,
            rwa5=3,
            rwa6=3
        )
        yield Submission(pages.End, check_html=False)
