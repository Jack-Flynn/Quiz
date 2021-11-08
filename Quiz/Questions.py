# Functions go here
def questions (question, answer):
    global ticks, strikes, questions_answered
    error = "please enter a whole number"
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if response == answer:
                # Congratulating a correct answer
                print("Good Job!")
                ticks += 1
                questions_answered += 1
                return response
            elif response != answer:
                # Encouraging to stay strong in the face of failure
                print("Unlucky! Better luck next time!")
                strikes += 1
                questions_answered += 1
                return response
        except ValueError:
            print(error)


# Main Routine here
ticks = 0
strikes = 0
questions_answered = 0

# Questions
while questions_answered != 5:
    question1 = questions("Question 1: What is the correct spelling of the fear of long words (sorry if you're dyslexic)?\n"
                          "1: hippopotomonstrosesquippedaliophobia\n"
                          "2: hippopotomonstrosesquippadeliophobia\n"
                          "3: hippopotomonstrosesquipadeliophobia", 1)
    question2 = questions("Question 2: What is a mineral consisting of a silicon dioxide that occurs in colourless and "
                          "transparent hexagonal crystals and also in crystalline masses?\n"
                          "1: Diamond\n"
                          "2: Gypsum\n"
                          "3: Quartz", 3)
    question3 = questions("Question 3:What is the rarest colour (yes these are all shades of a colour)? \n"
                          "1: Cochineal\n"
                          "2: Lapis Lazuli\n"
                          "3: Quercitron", 2)
    # If 3 questions wrong then stop code
    if strikes >= 3:
        print("That's 3 strikes! You're out!")
        break
    question4 = questions("Question 4: In what year did Australian rock band ICEHOUSE release the album 'Man Of Colours'?\n"
                          "1: 1982\n"
                          "2: 1987\n"
                          "3: 1984", 2)
    if strikes >= 3:
        print("That's 3 strikes! You're out!")
        break
    question5 = questions("Question 5: Who created the first algorithm designed to be read by a computer?\n"
                          "1: William Higinbotham\n"
                          "2: Alan Turing\n"
                          "3: Ada Lovelace", 3)

# Give feedback on how user went
if ticks > strikes:
    print("Well done! your correct:wrong ratio is {}:{}!".format(ticks, strikes))
elif strikes > ticks:
    print("What a disaster! Your correct:wrong ratio is {}:{}".format(ticks, strikes))
