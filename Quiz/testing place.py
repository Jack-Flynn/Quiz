def questions (question):
    strikes = 0
    ticks = 0
    questions_answered = 0
    response = input(question)
    if response == "a":
        print("well done 'a' was correct")
        ticks += 1
        questions_answered += 1
    else:
        print("you are wrong")
        strikes += 1
        questions_answered += 1

    if strikes == 3:
        print("That's 3 strikes! You're out!")
    elif questions_answered > 4:
        print("well now we're done aren't we?")
    print(strikes)
    print(ticks)
    print(questions_answered)

question_one = questions("Question 1: What is the correct spelling of the fear of long words (sorry if you're dyslexic)?\n"
                      "A: hippopotomonstrosesquippedaliophobia\n"
                      "B: hippopotomonstrosesquippadeliophobia\n"
                      "C: hippopotomonstrosesquipadeliophobia\n")
question_two = questions("Question 2: What is the correct spelling of the fear of long words (sorry if you're dyslexic)?\n"
                      "A: hippopotomonstrosesquippedaliophobia\n"
                      "B: hippopotomonstrosesquippadeliophobia\n"
                      "C: hippopotomonstrosesquipadeliophobia\n")
question_three = questions("Question 3: What is the correct spelling of the fear of long words (sorry if you're dyslexic)?\n"
                      "A: hippopotomonstrosesquippedaliophobia\n"
                      "B: hippopotomonstrosesquippadeliophobia\n"
                      "C: hippopotomonstrosesquipadeliophobia\n")
question_four = questions("Question 4: What is the correct spelling of the fear of long words (sorry if you're dyslexic)?\n"
                      "A: hippopotomonstrosesquippedaliophobia\n"
                      "B: hippopotomonstrosesquippadeliophobia\n"
                      "C: hippopotomonstrosesquipadeliophobia\n")
question_five = questions("Question 5: What is the correct spelling of the fear of long words (sorry if you're dyslexic)?\n"
                      "A: hippopotomonstrosesquippedaliophobia\n"
                      "B: hippopotomonstrosesquippadeliophobia\n"
                      "C: hippopotomonstrosesquipadeliophobia\n")

