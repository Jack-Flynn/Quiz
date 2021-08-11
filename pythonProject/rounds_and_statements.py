# Balance function here
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
    print("Balance: ", how_much)
    print()
    if how_much <= 0:
        print("you are broke! go home!")
        break

    play_again = input("Press <Enter> to play again or type 'quit' to exit").lower().strip()
