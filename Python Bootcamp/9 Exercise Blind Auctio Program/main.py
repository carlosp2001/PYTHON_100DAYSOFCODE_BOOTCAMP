from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
print("Welcome to the secret auction program.")
other_bid=True
bids={}
while other_bid==True:
  bidder=input("What is your name? ")
  bid=input("What is your bid? ")
  bids[bidder]=bid
  other_bidder=input("Are there any other bidders? Yes or No ").lower()
  if not other_bidder=="yes":
    other_bid=False
  clear()

max_bid=0
max_bidder=""
for key in bids:
  
  if int(bids[key])>max_bid:
    max_bid=bids[key]
    max_bidder=key
print(f"The winner is {max_bidder} with a bid of ${max_bid}")