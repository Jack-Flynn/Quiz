# Functions go here
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower().strip()

        if response in yes:
            response = "yes"
            return response

        elif response in no:
            response = "no"
            return response

        else:
            print("Please answer yes / no")

# Store all values for yes and no
yes = ["yes", "y", "affirmative", "positive", "correct", "yep", "yeah"]
no = ["no", "n", "wrong", "incorrect", "negative", "nah", "nope"]

instructions = yes_no("Have you played")
print(no_yes)
