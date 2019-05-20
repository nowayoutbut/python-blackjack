from functional import seq
import random
from cards import cards

def drawCard(count=1):
    pick = []

    for i in range(count):
        pick.append(cards.pop(0))

    return pick

userCards = [*drawCard(2)]
cpuCards = [*drawCard(2)]

def getTotal(cards):
    return seq(cards).reduce(lambda prev, card:prev+card["point"],0)

def showYourCards():
    for msg in seq(userCards).map(lambda card: card["symbol"]+" "+card["num"]).to_list():
        print(msg)
    
    print(">>")

    total = getTotal(userCards)
    print(">>total: "+str(total))


userState = "pending"
cpuState = "break"    


while userState != "break":
    showYourCards()
    take = input('do you take a card ? >> ')

    if(take == "t"):
       userCards.append(*drawCard(1))
       total = getTotal(userCards)
       if(total > 21):
           userState = "break"
           print("your cards total point is >>> "+str(total))
           print('You Lose...')

    elif(take == "b"):
        userState="break"
    