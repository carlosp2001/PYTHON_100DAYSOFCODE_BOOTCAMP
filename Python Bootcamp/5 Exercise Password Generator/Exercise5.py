#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
lettersspassword=list()
for i in range(0,nr_letters):
  lettersspassword.append(random.choice(letters))

numberspassword=list()
for i in range(0,nr_numbers):
  numberspassword.append(random.choice(numbers))

symbolsspassword=list()
for i in range(0,nr_symbols):
  symbolsspassword.append(random.choice(symbols))

password=[lettersspassword,symbolsspassword,numberspassword]

finalpassword=""
for i in password:
  for y in i:
    finalpassword+=str(y)
print("Ordernated Password")   
print(finalpassword)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
newrandompassword=list()
for i in finalpassword:
  newrandompassword.append(i)

randompassword=""
random.shuffle(newrandompassword)
for i in newrandompassword:
  randompassword+=str(i)
print("Random Password")   
print(randompassword)