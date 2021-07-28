def token_generator():
    from random import randint
    # generate some integers
    for _ in range(1):
        token = randint(1, 100)
    if token <= 25:
        print("Donkey")
    elif token > 25 and token <= 50:
        print("Horse")
    elif token > 50 and token <= 75:
        print("Zebra")
    else:
        print("Unicorn")
token_generator()


