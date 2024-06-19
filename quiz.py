questions = ("Which is the capital city of India?",
             "Which is the National fruit of India?",
             "Who is the first Prime Minister of India",
             "How many continents are there in the world?",
             "What is the opposite of happy?")

options = (("A. New Delhi","B. Mumbai", "C. Bangalore", "D.Hyderabad"),
           ("A. Banana","B. Apple", "C. Mango", "D. Apple"),
           ("A. Gandhiji","B. Nehru ", "C. Bharathiyar", "D. Kamarajar "),
           ("A. 4","B. 5", "C. 6", "D. 7"),
           ("A. Sad ","B. Pleasant", "C. Joy", "D. Good"))


answer = ("A", "C", "B", "D", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("What's your option(A,B,C,D)?: ").upper()
    guesses.append(guess)
    if guess == answer[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"The correct answers is {answer[question_num]}")
    question_num += 1

print()
print("    RESULTS     ")
print()

print("Answers: ", end="")
for answers in answer:
    print(answers, end=" ")
print()

print("GUESSES: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions)*100)
print(f"Your Score is: {score}%")
