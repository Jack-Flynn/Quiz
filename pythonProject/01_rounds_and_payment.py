# Ask for payment
print("Costs: $1 per round, up to 10 rounds")
payment = int(input("How much do you wish to pay?"))
if payment >= 1 and payment <= 10:
    print("Continue")
else:
    print("Please enter a whole number between 1 and 10")
