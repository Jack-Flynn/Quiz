# Functions go here
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower().strip()

        if response in yes:
            return response

        elif response in no:
            return response

        else:
            print("Please answer yes / no")


def questions (question, answer):
    # Bringing variables into function
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


# Variables and lists
yes = ["yes", "y", "affirmative", "positive", "correct", "yep", "yeah"]
no = ["no", "n", "wrong", "incorrect", "negative", "nah", "nope"]
ticks = 0
strikes = 0
questions_answered = 0

# Give colour
print("\033[1;32;40m")

# Greet user and ask whether or not to show instructions
print("Welcome to Quizzerino!")
instructions = yes_no("Have you played this quiz before?")

if instructions in no:
    print("You will be asked 5 questions with 3 possible choices. answer them with '1' '2' or '3'. \n"
          "If you get 3 questions wrong you will fail and have to try again. \n"
          "And the most important instruction of all: (try and)have fun! \n"
          "Oh and I thought I might mention that this quiz is rather challenging and unforgiving.")
elif instructions in yes:
    print("righty-ho moving on")

# Main Routine here

# Questions
while questions_answered != 5:
    question1 = questions("Question 1: What is the correct spelling of the fear of long words (sorry if you're dyslexic)?\n"
                          "1: hippopotomonstrosesquippedaliophobia\n"
                          "2: hippopotomonstrosesquippadeliophobia\n"
                          "3: hippopotomonstrosesquipadeliophobia", 1)
    question2 = questions("Question 2: What is a mineral consisting of a silicon dioxide that occurs in colourless and"
                          " transparent hexagonal crystals and also in crystalline masses?\n"
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
    print("Well done! your correct:wrong ratio is {}:{}! You did so well! Please play again!".format(ticks, strikes))
elif strikes > ticks:
    print("What a disaster! Your correct:wrong ratio is {}:{}."
          " Perhaps you could try again and improve your score?".format(ticks, strikes))
