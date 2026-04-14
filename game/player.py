import random
import time

class Player():

    def __init__(self,type="pc",cards=[],bet=0,name="",amount=0):

        self.name=name
        self.type=type
        self.cards=cards
        self._bet=bet
        self.amount=amount

def place_initial_bet(self):
        
        while True:
            amount=input(f"Place initial bet amount.Current amount is {self.amount}: ")

            if amount.isdigit():
                n=int(amount)
                if n>0 and n<=self.amount:
                    #self.amount=self.amount-n #use a setter 
                    self.bet=n
                    return n
                
                print("Invalid amount entered.")
                print(f"amount must range from 1 to {self.amount}")
                print("try again")
            
            else:
                print(f"enter a number as valid amount between 1 and {self.amount}")

   