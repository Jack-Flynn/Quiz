
# Generate some tokens
def token_generator():
    global token
    from random import randint
    # generate some integers
    for _ in range(1):
        token = randint(1, 100)
    if token <= 25:
        print("Donkey")
    elif 25 < token <= 50:
        print("Horse")
    elif 50 < token <= 75:
        print("Zebra")
    else:
        print("Unicorn")


token_generator()
