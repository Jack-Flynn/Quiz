def questions (question, answer):
    global ticks, strikes, questions_answered
    error = "please enter a number"

    try:
        response = int(input(question))
        if response == answer:
            print("Good Job!")
            ticks += 1
            questions_answered += 1
            return response
        elif response != answer:
            print("Unlucky! Better luck next time!")
            strikes += 1
            questions_answered += 1
    except ValueError:
        print(error)


ticks = 0
strikes = 0
questions_answered = 0
while strikes < 3 and questions_answered != 5:
    question1 = questions("Question 1: What is the correct spelling of the fear of long words (sorry if you're dyslexic)?\n"
                          "1: hippopotomonstrosesquippedaliophobia\n"
                          "2: hippopotomonstrosesquippadeliophobia\n"
                          "3: hippopotomonstrosesquipadeliophobia", 1)
    question2 = questions("Question 2: What is a mineral consisting of a silicon dioxide that occurs in colourless and transparent\n"
                          "hexagonal crystals and also in crystalline masses?\n"
                          "1: Diamond\n"
                          "2: Gypsum\n"
                          "3: Quartz", 3)
    question3 = questions("Question 3:What is the rarest colour (yes these are all shades of a colour)? \n"
                          "1: Cochineal\n"
                          "2: Lapis Lazuli\n"
                          "3: Quercitron", 2)
    question4 = questions("Question 4:\n"
                          "1: a\n"
                          "2: b\n"
                          "3: c", 1)
    question5 = questions("Question 5:\n"
                          "1: a\n"
                          "2: b\n"
                          "3: c", 1)

print(ticks)
print(strikes)
print(questions_answered)
