rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print("Your choice:\n")
if choice==0:
  print(rock+"\n")
if choice==1:
  print(paper+"\n")
if choice==2:
  print(scissors+"\n")

computerchoice=random.randint(0,2)
print("\nComputer choice:\n")
if computerchoice==0:
  print(rock+"\n")
if computerchoice==1:
  print(paper+"\n")
if computerchoice==2:
  print(scissors+"\n")

if computerchoice==choice:
  print("Draw")

if computerchoice==0 and choice==1:
  print("You win")
if computerchoice==0 and choice==2:
  print("Computer Wins")
if computerchoice==1 and choice==0:
  print("Computer Wins")
if computerchoice==1 and choice==2:
  print("You win")
if computerchoice==2 and choice==0:
  print("You win")
if computerchoice==2 and choice==1:
  print("Computers win")