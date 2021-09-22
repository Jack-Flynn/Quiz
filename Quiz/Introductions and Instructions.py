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

print("\033[1;32;40m")

# Store all values for yes and no
yes = ["yes", "y", "affirmative", "positive", "correct", "yep", "yeah"]
no = ["no", "n", "wrong", "incorrect", "negative", "nah", "nope"]

# Ask user whether or not to show instructions
print("Welcome to placeholderquizname!")
instructions = yes_no("Have you played this quiz before?")

if instructions in no:
    print("any details yet jack?")
elif instructions in yes:
    print("righty-ho moving on")
