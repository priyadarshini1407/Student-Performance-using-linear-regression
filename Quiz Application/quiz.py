# Quiz Application for UG/PG Students

questions = [
    {
        "question": "Who is the President of India?",
        "options": ["A. Narendra Modi", "B. Droupadi Murmu", "C. Jagdeep Dhankhar", "D. Amit Shah"],
        "answer": "B"
    },
    {
        "question": "Which country hosted the 2024 Summer Olympics?",
        "options": ["A. Japan", "B. USA", "C. France", "D. China"],
        "answer": "C"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Program Unit", "B. Central Processing Unit", "C. Computer Processing Unit", "D. Control Process Unit"],
        "answer": "B"
    },
    {
        "question": "Which organization supports the Python language?",
        "options": ["A. Microsoft", "B. Google", "C. Python Software Foundation", "D. IBM"],
        "answer": "C"
    },
    {
        "question": "Who is known as the Father of the Indian Constitution?",
        "options": ["A. Mahatma Gandhi", "B. Jawaharlal Nehru", "C. B. R. Ambedkar", "D. Sardar Patel"],
        "answer": "C"
    },
    {
        "question": "Which is the largest planet in the Solar System?",
        "options": ["A. Earth", "B. Saturn", "C. Jupiter", "D. Neptune"],
        "answer": "C"
    },
    {
        "question": "Which sport is associated with Wimbledon?",
        "options": ["A. Cricket", "B. Football", "C. Tennis", "D. Hockey"],
        "answer": "C"
    },
    {
        "question": "What does AI stand for?",
        "options": ["A. Automated Intelligence", "B. Artificial Intelligence", "C. Advanced Internet", "D. Automatic Information"],
        "answer": "B"
    },
    {
        "question": "Which Indian state is known as the 'Spice Garden of India'?",
        "options": ["A. Tamil Nadu", "B. Kerala", "C. Karnataka", "D. Goa"],
        "answer": "B"
    },
    {
        "question": "Which Indian organization conducts the Gaganyaan Mission?",
        "options": ["A. DRDO", "B. NASA", "C. ISRO", "D. HAL"],
        "answer": "C"
    }
]

score = 0
attempted = 0

print("=" * 50)
print("        WELCOME TO THE QUIZ")
print("=" * 50)

for i, q in enumerate(questions, start=1):
    print("\nQuestion", i)
    print(q["question"])

    for option in q["options"]:
        print(option)

    answer = input("Enter your answer (A/B/C/D) or press Enter to skip: ").upper()

    if answer != "":
        attempted += 1

    if answer == q["answer"]:
        print("Correct Answer!")
        score += 1
    elif answer == "":
        print("Question Skipped!")
    else:
        print("Wrong Answer!")
        print("Correct Answer:", q["answer"])

total_questions = len(questions)
wrong = attempted - score
not_attempted = total_questions - attempted
percentage = (score / total_questions) * 100

print("\n" + "=" * 50)
print("              QUIZ RESULT")
print("=" * 50)

print("Total Questions :", total_questions)
print("Attempted       :", attempted)
print("Not Attempted   :", not_attempted)
print("Correct Answers :", score)
print("Wrong Answers   :", wrong)
print("Score           :", score, "/", total_questions)
print("Percentage      :", round(percentage, 2), "%")

if percentage >= 80:
    print("Grade           : Excellent")
elif percentage >= 60:
    print("Grade           : Good")
elif percentage >= 40:
    print("Grade           : Average")
else:
    print("Grade           : Needs Improvement")

print("=" * 50)
print("Thank You for Participating!")
print("=" * 50)