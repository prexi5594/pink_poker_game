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



if __name__ == "__main__":
    game = Game()

    print("\n  Starting Poker Game...\n")

    print("=== FULL DECK ===")
    game.deck.print_deck()

    def show_pc_cards(player):
        print("\n=== PC CARDS ===")
        print("Card 1:")
        player.cards[0].print_card()
        print("Card 2: [Hidden] ")

    def show_human_cards(player):
        print("\n=== YOUR CARDS ===")
        for i, card in enumerate(player.cards[:2], start=1):
            print(f"Card {i}:")
            card.print_card()

    show_pc_cards(game.pc)
    show_human_cards(game.human)