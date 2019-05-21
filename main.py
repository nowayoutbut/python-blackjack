from cards import cards
from player import Player,Dealer


player = Player(cards)
dealer = Dealer(cards)

def showCards(player:Player)->None:
    print(">>"+"\n>>".join(player.show()))
    
    print(">>")

    total = player.total
    print(">>total: "+str(total))


while player.state == "pending" or dealer.state == "pending":
    showCards(player)
    take = input('do you take a card ? Y/n >> ')

    if(take == "Y"):
        player.draw(cards)
        total = player.total        
        if(total > 21):
           player.state = "break"

    elif(take == "n"):
        player.state="break"
    
    if(dealer.total < 21):
        print("Dealer take a card......")
        dealer.draw(cards)

        if(dealer.total > 21):
            dealer.state = "break"
    else:
        dealer.state = "break"


dealer_point = 21 - dealer.total 
player_point = 21 - player.total

print("Dealer total is "+str(dealer.total))
print("Your total is "+str(player.total))

if(dealer_point < 0 and player_point < 0):
    print(">>> This Game is draw")
elif(dealer_point >= 0 and player_point < 0):
    print(">>> You Lose......")

elif(dealer_point >= 0 and player_point >=0 and dealer_point <= player_point):
    print(">>> You Loose......")
else:
    print(">>> You Win!")