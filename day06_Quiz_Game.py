print("=== PYTHON QUIZ GAME ===")
print("Answer the following questions\n")

questions = [
    {
        "question": "Which language are we learning?",
        "options": ["A) Python", "B) Java", "C) C++", "D) JavaScript"],
        "answer": "A"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A) //", "B) /* */", "C) #", "D) --"],
        "answer": "C"
    },
    {
        "question": "What does 'IDE' stand for?",
        "options": ["A) Integrated Development Environment", "B) Internal Development Environment", "C) Integrated Design Environment", "D) Internal Design Environment"],
        "answer": "A"
    },
    {
        "question": "What is the output of print(2 + 3)?",
        "options": ["A) 5", "B) 23", "C) Error", "D) None"],
        "answer": "A"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A) func", "B) def", "C) function", "D) define"],
        "answer": "B"
    },
    {
        "question": "What is the correct way to create a list in Python?",
        "options": ["A) list = ()", "B) list = []", "C) list = {}", "D) list = <>"],
        "answer": "B"
    }
    
]

score = 0

for item in questions:
    print("\n" + item["question"])
    user_answer = input("Your answer (A, B, C, D): ").strip().upper()
    if user_answer == item["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    for option in item["options"]:
        print(option)
    print()

print("\n=== QUIZ COMPLETE ===")
print(f"Your final score is: {score}/{len(questions)}")

percentage = (score / len(questions)) * 100
print(f"You scored {percentage:.0f}% on the quiz.")