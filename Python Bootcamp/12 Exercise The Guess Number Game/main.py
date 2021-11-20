#Number Guessing Game Objectives:
from art import logo

import random
# Include an ASCII art logo.

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

Easy_level=10
Hard_level=5



def make_a_guess(actualanswer,randomnumber,attemps):
  if actualanswer>randomnumber:
    print("Too high\nGuess again")
    return attemps-1
  elif actualanswer<randomnumber:
    print("Too low\nGuess again")
    return attemps-1
  elif actualanswer==randomnumber:
    print(f"You got it! The answer was {randomnumber}.")
    
def set_difficulty():
  difficulty=input("Choose a difficulty. Type 'easy' or 'hard' \n")
  if difficulty=='easy':
    return Easy_level
  elif difficulty=='hard':
    return Hard_level

def game():
  randomnumber=random.randint(1,100)
  print("Welcome to the Number Guessing Game ")
  print("I'm thinking of a number between 1 and 100.")
  attemps=set_difficulty()

  actualanswer=0
  while actualanswer!=randomnumber and attemps>0:
    print(f"You have {attemps} attemps remaining to guess the number")
    actualanswer=int(input("Make a guess:  "))
    attemps=make_a_guess(actualanswer,randomnumber,attemps)
    if attemps==0:
      print("You've run out of lives")

play_again=True    
while play_again:
  
  print(logo)
  game()
  decision=input("Do you want to play again? 'y' for Yes 'n' for not ").lower()
  if decision=='n':
    play_again=False