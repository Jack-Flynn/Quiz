# Ask users for a number
get_number = int(input("Choose a number? "))

# Multiply the number by 5
times_five = get_number * 5

# Output the result
print("{} times five is equal to {}".format(get_number, times_five))


# Get name until exit code is entered

name = ""
while name.lower() != "xxx":
	name = input("Who are you? ")
	print(name)

print()
print("We are done!")
