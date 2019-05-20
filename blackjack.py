from functional import seq
import random

symbols = ["Heart", "Spade", "Diamond", "Clover"]
points = [
    {"num":"A","point":11}, 
    {"num":"K","point":10},
    {"num":"Q","point":10},
    {"num":"J","point":10},
    {"num":"10","point":10},
    {"num":"9","point":9},
    {"num":"8","point":8},
    {"num":"7","point":7},
    {"num":"6","point":6},
    {"num":"5","point":5},
    {"num":"4","point":4},
    {"num":"3","point":3},
    {"num":"2","point":2},
]


def createCards(symbol):
    return seq(points).map(lambda point: {**point, "symbol": symbol})

cards = seq(symbols).map(createCards).flatten().to_list()
random.shuffle(cards)

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
    