from typing import List
from functional import seq

class Player:
    _cards:List[object] = []
    state = "pending"

    def __init__(self,cards)->None:
        self.draw(cards, 2)

    
    def draw(self,cards, count=1)->None:

        for i in range(count):
            self._cards.append(cards.pop(0))
    
    @property
    def total(self)->int:
        return seq(self._cards).reduce(lambda prev, card:prev+card["point"],0)    
    
    
    def show(self)->List[str]:
        return seq(self._cards).map(lambda card: card["symbol"]+" "+card["num"]).to_list()
    