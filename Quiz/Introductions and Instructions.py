# Functions go here
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower().strip()

        if response in yes:
            return response

        elif response in no:
            return response

        else:
            print("Please answer yes / no")

# Give colour
print("\033[1;32;40m")

# Store all values for yes and no
yes = ["yes", "y", "affirmative", "positive", "correct", "yep", "yeah"]
no = ["no", "n", "wrong", "incorrect", "negative", "nah", "nope"]

# Ask user whether or not to show instructions
print("Welcome to placeholderquizname!")
instructions = yes_no("Have you played this quiz before?")

if instructions in no:
    print("You will be asked 5 questions with 3 possible choices. answer them with '1' '2' or '3'. \n"
          "If you get 3 questions wrong you will fail and have to try again. \n"
          "and the most important instruction of all: Have fun! \n"
          "Oh and I thought I might mention that this quiz is rather challenging and unforgiving.")
elif instructions in yes:
    print("righty-ho moving on")
