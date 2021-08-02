# Greet the user
print("Welcome to Lucky Unicorns!")
show_instructions = input("Have you played before?").strip().lower()
if show_instructions == "yes" or show_instructions == "y":
    print("Have fun!")
elif show_instructions == "no" or show_instructions == "n":
    print("You will pay a amount of up to $10 (with a minimum of $1)")
    print("You will then be given a token")
    print("If your token is a donkey then, bad luck, you lose, but if it is a horse or a zebra then you win 50c")
    print("If your token is a unicorn then you win $5")
