strikes = 0
ticks = 0
questions_answered = 0
while questions_answered < 5 and strikes != 3:
    question1 = input("what is the answer to this question?").strip().lower()
    if question1 == "answer":
        print("correct!")
        ticks += 1
        questions_answered += 1
    elif question1 == "rewsna":
        print("what are you even thinking?")
        strikes += 1
        questions_answered += 1
    else:
        print("you suck!")
        strikes += 1
        questions_answered += 1

print(strikes)
print(ticks)
print(questions_answered)
