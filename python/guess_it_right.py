
print("Welcome to the QUIZ! I am going to ask you 5 questions.")
welcome = input("Are you ready? (Y/N): ").upper()
if welcome == 'Y':
    print('Let us begin!')
    print('-----^^-----')
else:
    print('pussio')
    quit()


questions = ("Choose a sentence in the past simple: ",
                       "Where is 'a' used correctly?: ",
                       "How many letters are there in the alphabet?: ",
                       "What's your teacher's name?: ",
                       "What's a 'disciple'?: ")

options = (("A. I am going home.", "B. Mr. Alexander had not had a hat.", "C. She was well known for her beauty.", "D. She's qualified enough."),
                   ("A. I may not not a flowers", "B. Should we call you a emperor?", "C. Elephants tend to stay in groups.", "D. I am just not a peasantly behaving crone."),
                   ("A. 24", "B. 33", "C. 32", "D. 26"),
                   ("A. Pol", "B. Paul", "C. Paulo", "D. Pablo"),
                   ("A. Дисциплина", "B. Апостол", "C. Раздел книги", "D. Дисциплинировать"))

answers = ("C", "D", "D", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("correct answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("your guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"You scored {score}%")