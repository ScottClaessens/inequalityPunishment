from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
from otree.api import Submission
import random

class PlayerBot(Bot):
    def play_round(self):
        yield pages.Demographics, dict(
            gender="Male",
            age=26,
            ethnicity='White',
            employed="Yes",
            married="Yes",
            religious="Yes",
            education=6,
            income=2,
            fair=3
        )
        yield pages.Survey, dict(
            sdo1=random.randint(1, 5),
            sdo2=random.randint(1, 5),
            sdo3=random.randint(1, 5),
            sdo4r=random.randint(1, 5),
            sdo5r=random.randint(1, 5),
            sdo6r=random.randint(1, 5),
            rwa1=random.randint(1, 5),
            rwa2=random.randint(1, 5),
            rwa3=random.randint(1, 5),
            rwa4r=random.randint(1, 5),
            rwa5r=random.randint(1, 5),
            rwa6r=random.randint(1, 5),
            attention=5
        )
        yield pages.Feedback, dict(feedback="This is a test")
        yield Submission(pages.End, check_html=False)
