from game_data import data
import random
import art
import replit

data_used=list()
score=0

def get_a_rival():
  global data_used
  different_rival=True
  while different_rival:
    indexrandom=random.choice(range(len(data)))
    if not indexrandom in data_used: 
      different_rival=False
  actualcelebrity=data[indexrandom] 
  data_used.append(indexrandom)
  return actualcelebrity

def highest_follower1(actual_celebrity,actualvs):
  if actual_celebrity["follower_count"]>actualvs["follower_count"]:
    return "a"
  elif actual_celebrity["follower_count"]<actualvs["follower_count"]:
    return "b"
  else:
    return None
    
game_continue=True
actualcelebrity=get_a_rival()

while game_continue:
  replit.clear()
  print(art.logo)
  if score>0:
    print(f"You're right! Current score: {score} .")
  print(f"Compare A: {actualcelebrity['name']}, a {actualcelebrity['description']}, from {actualcelebrity['country']}")
  print(art.vs)
  actualvs=get_a_rival()
  print(f"Compare B: {actualvs['name']}, a {actualvs['description']}, from {actualvs['country']}")
  decision=(input("Who has more followers? Type 'A' or 'B': ").lower())
  highest_follower=highest_follower1(actualcelebrity,actualvs)
  if highest_follower==decision:
    score+=1
    actualcelebrity=actualvs
  else:
    replit.clear()
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {score}")
    game_continue=False