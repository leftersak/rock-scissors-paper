from random import randrange

computer_input=["rock", "scissors", "paper"]
player_wins=0
computer_wins=0
round=0
history=[]
while player_wins!=3 and computer_wins!=3:
    #eisodos paixti
    
    player=input("Select rock, scissors, paper: ")
    while player!="scissors" and player!="paper" and player!="rock":
        player=input("Select rock, scissors, paper: ")

    #epilogi ipologisti
    i=randrange(0,3)

    #elegxos nikiti kai ektiposi apotelesmatos
    if player=="paper":
        if computer_input[i]=="paper":
            winner="No winner !"
        elif computer_input[i]=="rock":
            winner="Player won"
            player_wins+=1
        else:
            winner="Computer won!"
            computer_wins+=1
    elif player=="rock":
        if computer_input[i]=="paper":
            winner="Computer won!"
            computer_wins+=1
        elif computer_input[i]=="rock":
            winner="No winner! " 
        else:
            winner="Player won!"
            player_wins+=1
    else:#player:scissors
        if computer_input[i]=="paper":
            winner="Player won!"
            player_wins+=1
        elif computer_input[i]=="rock":
            winner="Computer won! " 
            computer_wins+=1
        else:
            winner="No winner!"
    round+=1
    
#ektiposi istorikou
    history.append("Round " + str(round) + ": Player: " + player + ", " "Computer: " + computer_input[i] + ", " + "Score: " + str(player_wins) + " - " + str(computer_wins))
    print(history)
if player_wins==3:
    print("Player won: " + str(player_wins) + " - " + str(computer_wins))
    for items in history:
        print(items)
else:
    print("Computer won: "   + str(computer_wins) + " - " + str(player_wins))
    for items in history:
        print(items)