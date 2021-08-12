# Functions here
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
        print("Donkey")
    elif 50 < token <= 75:
        print("Horse")
    elif 75 < token <= 90:
        print("Zebra")
    else:
        print("Unicorn")


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
        print("you are broke! go home!")
        break

    play_again = input("Press <Enter> to play again or type 'quit' to exit").lower().strip()
