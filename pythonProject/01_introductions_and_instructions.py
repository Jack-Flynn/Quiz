# Greet the user
print("Welcome to Lucky Unicorns!")


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
# Main routine goes here...


show_instructions = yes_no("Have you played the game before?")

if show_instructions == "no" or show_instructions == "n":
    print("You will pay a amount of up to $10 (with a minimum of $1)")
    print("You will then be given a token")
    print("If your token is a donkey then, bad luck, you lose, but if it is a horse or a zebra then you win 50c")
    print("If your token is a unicorn then you win $5")

elif show_instructions == "yes" or show_instructions == "y":
    print("OK! Moving on!")
print()
