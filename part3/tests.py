from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
from otree.api import Submission


class PlayerBot(Bot):
    def play_round(self):
        yield pages.Demographics, dict(
            gender="Male",
            age=26,
            ethnicity='White',
            employed="Yes",
            married="Yes",
            education=6,
            income=2,
            fair=3
        )
        yield pages.Survey, dict(
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
