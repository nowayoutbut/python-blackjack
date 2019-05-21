from typing import List
from cards import Card
from functional import seq

class Player:
    _cards:List[Card]
    state = "pending"

    def __init__(self,cards:List[Card])->None:
        self._cards = []
        self.draw(cards, 2)

    
    def draw(self,cards:List[Card], count=1)->None:

        for i in range(count):
            self._cards.append(cards.pop(0))
    
    @property
    def total(self)->int:
        return seq(self._cards).reduce(lambda prev, card:prev+card["poin"],0)    
    
    
    def show(self)->List[str]:
        return seq(self._cards).map(lambda card: card["symbol"]+" "+card["num"]).to_list()
    

class Dealer(Player):
    def empty(self):
        pass

