import os
import random
#from replit import clear
from subprocess import call

def clear():
    # check and make call for specific operating system
    _ = call('clear' if os.name =='posix' else 'cls')

##########################################
## The jack/queen/king all count as 10
## The ace can count as 11 or 1
##########################################
card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Player defines moneypool to play with
bank = int(input("With how much money to you want to enter the table?: $"))

#Start Game
def black_jack_game(bank):
    if bank < 5: #check if the player has enough money to play
        print("Sorry, you have to bet at least 5$.\nCome back when you have more money.")
        exit()
    keep_playing = "YES"

    #GAME LOOP
    while keep_playing == "YES":
        clear()
        print(f"You have {bank}$ in your bank.")
        bet = int(input("Make your bet: ")) #Make a bet / sets money in the pool
        while bet > bank:#denies a bet that is larger than the players money left
            clear()
            print(f"Your bet would exceed your bank.\nThere are only {bank}$ left.\nMake another bet")
            bet = int(input("Make your bet: "))
        #Dealer gets 1 card
        dealer_cards = []
        dealer_card = random.choice(card_deck)
        dealer_cards.append(dealer_card)
        sum_dealer_cards = sum(dealer_cards)
        print("\nDEALER:")
        print(f"{dealer_cards} Total: {sum_dealer_cards}")

        #We get 2 cards
        your_cards = []
        your_card = random.choice(card_deck)
        your_cards.append(your_card)
        your_card = random.choice(card_deck)
        your_cards.append(your_card)
        sum_your_cards = sum(your_cards)
        print("\nYOU:")
        print(f"{your_cards} Total: {sum_your_cards}")

        #Our/Player turn. Entering "HIT" gives us another card
        player_command = "HIT"
        check_scores = True
        while player_command == "HIT":
            player_command = input("Type 'HIT' for another card. Otherwise 'STAND':\n").upper()
            if player_command == "HIT":
                your_card = random.choice(card_deck)
                your_cards.append(your_card)
                sum_your_cards = sum(your_cards)
                print("\nYOU:")
                print(f"{your_cards} Total: {sum_your_cards}")
                if sum_your_cards > 21 and 11 in your_cards: #when you have exceeded 21 but have an ace. 11 turns to 1
                    for index, card in enumerate(your_cards):
                        if card == 11:
                            your_cards[index] = 1
                            break
                    sum_your_cards = sum(your_cards)
                    print("Ace converted from 11 to 1")
                    print(f"{your_cards} Total: {sum_your_cards}")
                elif sum_your_cards > 21: #when you have exceeded 21. we have lost
                    print("BUST. You lost")
                    check_scores = False
                    player_command = "STAND"
                    bank = bank - bet
                    print(f"You lost {bet}$. Your bank is now at {bank}$.")
                    keep_playing = input("Type 'yes' to keep playing, or 'no' to cash out:\n").upper()
            else: #player entered "STAND": Thus finishing our turn
                print("\n\n")

                #Dealer/AI logic
                if sum_your_cards < 22:
                    while sum_dealer_cards < 17: #while the bank has less than 17. it will get another card.
                        dealer_card = random.choice(card_deck)
                        dealer_cards.append(dealer_card)
                        sum_dealer_cards = sum(dealer_cards)
                        print("\nDEALER:")
                        print(f"{dealer_cards} Total: {sum_dealer_cards}")
                        keep_playing = "NO"
                        if sum_dealer_cards > 21 and 11 in dealer_cards: #when dealer has exceeded 21 but has an ace. 11 turns to 1
                            for index, card in enumerate(dealer_cards):
                                if card == 11:
                                    dealer_cards[index] = 1
                                    break
                            sum_dealer_cards = sum(dealer_cards)
                            print("\nAce converted from 11 to 1")
                            print(f"{dealer_cards} Total: {sum_dealer_cards}")
                        elif sum_dealer_cards > 21: #if House exceeds 21: We have won
                            print("HOUSE BUST")
                            check_scores = False
                            bank = bank + bet
                            print(f"You won {bet}$. Your bank is now at {bank}$.")
                            keep_playing = input("Type 'yes' to keep playing, or 'no' to cash out:\n").upper()

        #Checking who has a higher score
        if check_scores == True:
            if sum_dealer_cards > sum_your_cards:
                print("DEALER WINS.")
                bank = bank - bet
                print(f"You lost {bet}$. Your bank is now at {bank}$.")
                keep_playing = input("Type 'yes' to keep playing, or 'no' to cash out:\n").upper()
            elif sum_dealer_cards < sum_your_cards:
                bank = bank + bet
                print(f"You won {bet}$. Your bank is now at {bank}$.")
                keep_playing = input("Type 'yes' to keep playing, or 'no' to cash out:\n").upper()
            else:
                print("DRAW.")
                print(f"Your bank is still at {bank}$.")
                keep_playing = input("Type 'yes' to keep playing, or 'no' to cash out:\n").upper()

        #Player enters 'NO' and wants to end the game.
        if keep_playing == "NO":
            print(f"\nYour cashout is {bank}$.\nThank you for playing.")

black_jack_game(bank)