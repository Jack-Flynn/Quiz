#Define Variables
name = input("What is your name?")


#Get some random numbers
from random import randint
# generate some integers
for _ in range(1):
	winnings = randint(1, 10)

#Greet the user
print("Hello {} how do you feel playing Sandbox!".format(name))
print("That wasn't a question because we own your life!")
