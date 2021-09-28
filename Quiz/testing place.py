def question1 (question):
        response = input(question).lower().strip()

        if response == "a":
            print("well done 'a' was correct")
            ticks += 1
            questions_answered += 1
        else:
            print("you are wrong")
            strikes += 1
            questions_answered += 1
strikes = 0
ticks = 0
questions_answered = 0
question_one = question1("Question 1: What is the correct spelling of the fear of long words (sorry if you're dyslexic)?\n"
                      "A: hippopotomonstrosesquippedaliophobia\n"
                      "B: hippopotomonstrosesquippadeliophobia\n"
                      "C: hippopotomonstrosesquipadeliophobia").strip().lower()
if strikes == 3:
    print("That's 3 strikes! You're out!")
elif questions_answered > 4:
    print("well now we're done aren't we?")
print(strikes)
print(ticks)
print(questions_answered)
