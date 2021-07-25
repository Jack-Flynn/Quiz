# Functions go here...
def yes_no(question):...

def instructions():
    print("**** How to Play ****")
    print()
    print("The rules of the game go here")
    print()
    return ""

# Main routine goes here...
show_instructions = yes_no("Have you played the game before?")

if show_instructions == "yes":
    instructions()

print("Program continues")
