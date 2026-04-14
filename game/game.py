from deck import Deck
from player import Player


class Game():
    
    def __init__(self):
        self.pot=0
        deck=Deck()
        deck.shuffle()
        deck.shuffle()
        human_cards= [deck.give_card(),deck.give_card()]
        pc_card=[deck.give_card(),deck.give_card()]
        
        
        self.human=Player(type="human",
                          cards=human_cards,
                          bet=0,
                          name="John",amount=2000)
        self.pc=Player(type="pc",
                          cards=pc_card,
                          bet=0,
                          name="Stockfish",amount=2000)
        self._turn=self.human
        self.deck=deck
    
    @property
    def turn(self):
        return self._turn
    
    @turn.setter
    def turn(self,player):

        if isinstance(player,Player):
            self._turn=player
        
        else:
            raise ValueError("The turn must be assined to a player object")
