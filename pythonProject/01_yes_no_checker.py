# Ask the user if they have played before
show_instructions = input("Have you played this game before?").lower().strip()
# If they say yes, output 'program continues'
if show_instructions == "yes" or show_instructions == "y":
    print("Program continues")
# If they say no, output 'display instructions'
elif show_instructions == "no" or show_instructions == "n":
    print("Display information")
else:
    print("Please answer yes or no")
