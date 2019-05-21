from cards import cards
from player import Player


user = Player(cards)


def showYourCards(player:Player)->None:
    print(">>"+"\n>>".join(player.show()))
    
    print(">>")

    total = player.total
    print(">>total: "+str(total))


while user.state == "pending":
    showYourCards(user)
    take = input('do you take a card ? Y/n >> ')

    if(take == "Y"):
        user.draw(cards)
        total = user.total        
        if(total > 21):
           user.state = "break"
           print("your cards total point is >>> "+str(total))
           print('You Lose...')

    elif(take == "n"):
        user.state="break"
     
