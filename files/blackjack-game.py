# Import og ændring af random kommandoen
from random import choice as rc

def total(hand):
    Aces = hand.count(11)
    t = sum(hand)
    if t > 21 and Aces > 0:
        while Aces > 0 and t > 21:
            t -= 10
            Aces -= 1
    return t


# Kort udstillet i numre
kort = [2,3,4,5,6,7,8,9,10,10,10,10]

# Winstreak/score
cwin = 0
pwin = 0

while True:
    # Spillerens hånd
    player = []
    player.append(rc(kort))
    player.append(rc(kort))
    pbust = False
    cbust = False
    
    while True:
        # Spillerens hånd som bliver printed, plus lagt sammen så man får den samlede værdi
        tp = total(player)
        print("Your given cards are %s with a total value of [%d]" % (player, tp))
        if tp > 21:
            print("--> You have busted!")
            pbust = True
            break
        
        elif tp == 21:
            print("You have gotten the legendary blackjack, you have therefore won the game!")
            print()
            print("You WIN")
            break
        
        else:
            turn = input("Do you want to [Hit] or [Stand]? ").lower()
            if turn in ['hit', 'Hit', 'HIT']:
                player.append(rc(kort))
                print()
            elif turn in ['stand', 'Stand', 'STAND']:
                print()
                break
            else:
                print("Please input a valid answer")
                print()
                
    while True:
        # Computerens hånd
        computer = []
        computer.append(rc(kort))
        computer.append(rc(kort))
        while True:
            # Beksrivelse af computerens hånd, hvor at dens hånd skal være over 18 for at [Stand]
            tc = total(computer)
            if tc < 18:
                computer.append(rc(kort))
            else:
                break
        print("The computers given cards are %s with a total value of [%d]" % (computer, tc))
        print()

        # Kommandoen som finder ud af om både pc og spiller er gået over 21
        if tp > 21 and tc > 21:
            print()
            print("----------------------------------------------------------------------")
            print()
            print("You have both busted!")
            print("The game has ended in a draw!")
            print()
            
        # Kommandoen som finder ud af om computerens spillehånd er over 21
        elif tc > 21:
            print("--> The computer has busted!")
            print()
            cbust = True
            # Anden del af koden, som finder ud af om spilleren er busted. Hvis nej, så vinder spilleren.
            if pbust == False:
                print("----------------------------------------------------------------------")
                print()
                print("The player has won the game!")
                print()
                print("----------------------------------------------------------------------")
                print()
                print("You WIN")
                print()
                pwin += 1
                
        # Kommandoen som finder ud af om computerens hånd er højere end spillerens men stadigvæk under 22
        elif tc > tp:
            print("----------------------------------------------------------------------")
            print()
            print("The computer has won the game!")
            print()
            print("----------------------------------------------------------------------")
            print()
            print("You LOSE")
            print()
            cwin += 1

        # Kommandoen som finder ud af om både spillerens og computerens hånd er det samme. Hvor spillet ender med at stå lige
        elif tc == tp:
            print("----------------------------------------------------------------------")
            print()
            print("The game has ended in a draw!")

        # Kommandoen som aktivere hvis ingen af de øvre fylder kravene
        elif tp > tc:
            # Kommandoen som finder ud af om spillerens hånd er over computerens, men stadigvæk under 22
            if pbust == False:
                print("----------------------------------------------------------------------")
                print()
                print("The player has won the game!")
                print()
                print("----------------------------------------------------------------------")
                print()
                print("You WIN")
                print()
                pwin += 1

            # Kommandoen som finder ud af om computeren er busted og giver et output omkring at spilleren har tabt.
            elif cbust == False:
                print("----------------------------------------------------------------------")
                print()
                print("The computer has won the game!")
                print()
                print("----------------------------------------------------------------------")
                print()
                print("You LOSE")
                print()
                cwin += 1
            
        break

    
    print
    print("----------------------------------------------------------------------")
    print("WIN STREAK")
    print()
    print("Player = %d games" % (pwin))
    print("Computer = %d games" % (cwin))
    print()
    print("----------------------------------------------------------------------")
    print()
    exit1 = input("Press [ENTER] to play again or type quit to exit game ").lower()
    print()
    print("----------------------------------------------------------------------")
    if exit1 in ['quit', 'Quit', 'QUIT']:
        break
    print()
print()
print("Thanks for playing!")










                       
