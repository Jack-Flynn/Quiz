def questions (question, answer):
    global ticks, strikes, questions_answered
    error = "please enter a number"

    try:
        response = int(input(question))
        if response == answer:
            print("Correct")
            ticks += 1
            questions_answered += 1
            return response
        else:
            print("incorrect")
            strikes += 1
            questions_answered += 1
    except ValueError:
        print(error)


ticks = 0
strikes = 0
questions_answered = 0
while strikes != 3 and questions_answered != 5:
    question1 = questions("Question 1:\n""1: a\n""2: b\n""3: c", 1)
    question2 = questions("Question 2:\n""1: a\n""2: b\n""3: c", 1)
    question3 = questions("Question 3:\n""1: a\n""2: b\n""3: c", 1)
    question4 = questions("Question 4:\n""1: a\n""2: b\n""3: c", 1)
    question5 = questions("Question 5:\n""1: a\n""2: b\n""3: c", 1)

print(ticks)
print(strikes)
print(questions_answered)
