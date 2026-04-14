import random
import time

class Player():

    def __init__(self,type="pc",cards=[],bet=0,name="",amount=0):

        self.name=name
        self.type=type
        self.cards=cards
        self._bet=bet
        self.amount=amount
