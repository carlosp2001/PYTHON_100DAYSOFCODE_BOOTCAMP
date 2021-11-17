############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


import random
from art import logo
import replit

def add_card(list,cards):
  card=random.choice(cards)
  list.append(card)
  return card





decision=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if decision=="y":
  
  want_to_play=True
  while want_to_play: 
    user=list()
    computer=list()
    for i in range(1,3):
      add_card(user,cards)
      add_card(computer,cards)
    replit.clear() 
    print(logo) 
    current_score_user=user[0]+user[1]
    current_score_computer=computer[0]+computer[1]
    user_get_another=True


    while user_get_another:
      print(f"  Your cards: {user}, current score: {current_score_user}")
      print(f'  Computer first card {computer[0]}')
      if input("Type 'y' to get another card, type 'n' to pass: ").lower()=="y":      
        card=add_card(user,cards)
        current_score_user+=card
        if current_score_user>21 or current_score_user==21:
          user_get_another=False
      else:
        user_get_another=False

    computer_get_another=[True,False]
    
    while computer_get_another:
      if random.choice(computer_get_another)==True:      
        card=add_card(computer,cards)
        current_score_computer+=card
        if current_score_computer>21 or current_score_computer==21:
          computer_get_another=False  
      else:
        computer_get_another=False

    print(f"Your final hand: {user} final score: {current_score_user}")
    print(f"Computer final hand {computer} final score: {current_score_computer}")

    if current_score_user==current_score_computer:
      print("Draw")
    elif current_score_user==21:
      print("You win")
    elif current_score_computer==21 or (current_score_computer<21 and current_score_computer>current_score_user) or (current_score_computer>21 and current_score_computer<current_score_user):
      print("Computer Wins")
    else:
      print("You win")    

    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()=="y":
      want_to_play=True
    else:
      want_to_play=False
    

    
    
      

        
       







##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

