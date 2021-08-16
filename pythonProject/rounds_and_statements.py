# Functions go here
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower().strip()
        if response == "yes" or response == "y":
            response = "yes"
            return response
        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print("Please answer yes / no")

def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10"

    valid = False
    while not valid:
        try:
            response = int(input(question))
            if low < response <= high:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

def token_generator():
    global token
    from random import randint
    # generate some integers
    for _ in range(1):
        token = randint(1, 100)
    if token <= 50:
        print("Bad luck, you got a Donkey, you win nothing and lose nothing.")
    elif 50 < token <= 80:
        print("You got a Horse! You win 50 cents!")
    elif 80 < token <= 95:
        print("You got a Zebra! You win 50 cents!")
    else:
        print("What incredible luck! you got a Unicorn! You win 5 dollars!")


# Greet the user
print("Welcome to Lucky Unicorns!")

show_instructions = yes_no("Have you played the game before?")

if show_instructions == "no" or show_instructions == "n":
    print("You will pay a amount of up to $10 (with a minimum of $1)")
    print("You will then be given a token")
    print("If your token is a donkey then, bad luck, you lose, but if it is a horse or a zebra then you win 50c")
    print("If your token is a unicorn then you win $5")
    print("OK! We are ready to continue now!")
elif show_instructions == "yes" or show_instructions == "y":
    print("OK! Moving on!")
print()

# Ask for payment
how_much = num_check("How much would you like to play with?", 0, 10)

rounds_played = 0

play_again = input("Press <Enter> to play...").lower().strip()
while play_again != "quit":

    # Increase # of rounds played
    rounds_played += 1

    # Print round number
    print()
    print("*** Round #{} ***".format(rounds_played))
    how_much -= 1
    token_generator()
    if token <= 50:
        how_much += 0
    elif 50 < token <= 75:
        how_much += 0.5
    elif 75 < token <= 90:
        how_much += 0.5
    else:
        how_much += 5
    print("Balance: ", how_much)
    print()

    if how_much <= 0:
        print("You have ran out of money and cannot play any more rounds!")
        break

    play_again = input("Press <Enter> to play again or type 'quit' to exit").lower().strip()
    if play_again == "quit":
        print("Exiting code!")
        break
