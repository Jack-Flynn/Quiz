strikes = 0
ticks = 0
questions_answered = 0
while questions_answered < 5 and strikes != 3:
    question1 = input("Question 1: What is the correct spelling of the fear of long words (sorry if you're dyslexic)?\n"
                      "A: hippopotomonstrosesquippedaliophobia\n"
                      "B: hippopotomonstrosesquippadeliophobia\n"
                      "C: hippopotomonstrosesquipadeliophobia").strip().lower()
    if question1 == "a":
        print("Very nicely done!")
        ticks += 1
        questions_answered += 1
    else:
        print("Unlucky! better luck next time!")
        strikes += 1
        questions_answered += 1

    question2 = input("What is a mineral consisting of a silicon dioxide that occurs in colourless and transparent\n"
                      "hexagonal crystals and also in crystalline masses?\n"
                      "A: Diamond\n"
                      "B: Gypsum\n"
                      "C: Quartz")
    if question2 == "c":
        print("Well done you geologist!")
        ticks += 1
        questions_answered += 1
    else:
        print("Unlucky! better luck next time!")
        strikes += 1
        questions_answered += 1

    question3 = input("What is the rarest colour (yes these are all shades of a colour)? \n"
                      "A: Cochineal\n"
                      "B: Lapis Lazuli\n"
                      "C: Quercitron")
    if question3 == "b":
        print("Good job!")
        ticks += 1
        questions_answered += 1
    else:
        print("Unlucky! better luck next time!")
        strikes += 1
        questions_answered += 1

    question4 = input("placeholder")
    if question4 == "place":
        print("Good job!")
        ticks += 1
        questions_answered += 1
    else:
        print("Unlucky! better luck next time!")
        strikes += 1
        questions_answered += 1

    question5 = input("placeholder")
    if question5 == "holder":
        print("Good job!")
        ticks += 1
        questions_answered += 1
    else:
        print("Unlucky! better luck next time!")
        strikes += 1
        questions_answered += 1

    if strikes == 3:
        print("That's 3 strikes! You're out!")
    elif questions_answered > 4:
        print("well now we're done aren't we?")
print(strikes)
print(ticks)
print(questions_answered)
