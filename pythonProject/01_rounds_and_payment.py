# Ask for payment
print("Costs: $1 per round, up to 10 rounds")
def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10"

    valid = False
    while not valid:
        try:
            response = int(input(question))

            if low < response  <= high:
                return response

            else:
                print(error)

        except ValueError:
            print(error)
how_much = num_check("How much would you like to play with?", 0, 10)

