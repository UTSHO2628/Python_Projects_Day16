import random

# Questions (You can add and change more question in this project)
flashcards = {
    "What is the default value of a boolean in Java?": "False",
    "Which keyword is used to create objects in Java?": "new",
    "Which data type is used for decimal numbers?": "double",
    "What is the default value of an object reference variable?": "null",
    "Which collection class allows duplicates in Java?": "ArrayList"
}

# point count
score = 0

# question changing 
questions = list(flashcards.keys())
random.shuffle(questions)

# ask question and check answer
for question in questions:
    print(question)
    user_answer = input("Your answer: ")

    if user_answer.lower() == flashcards[question].lower():
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is: {flashcards[question]}\n")

# show your total point
print(f"Your total score is: {score}/{len(flashcards)}")
