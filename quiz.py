question_bank = [
    {
        "text": "What is the capital of India?",
        "answer": "A"
    },
    {
        "text": "Which language is used for web development?",
        "answer": "B"
    },
    {
        "text": "What is 2 + 2?",
        "answer": "C"
    },
    {
        "text": "Which one is a programming language?",
        "answer": "D"
    }
]

options = [
    ["A. Delhi", "B. Mumbai", "C. Chennai", "D. Hyderabad"],
    ["A. Python", "B. HTML", "C. C++", "D. All of these"],
    ["A. 3", "B. 5", "C. 4", "D. 6"],
    ["A. Google", "B. Facebook", "C. YouTube", "D. Python"]
]


print("************************")
print("Welcome to My Quiz Game!!!")
print("************************")

score = 0


def check_answer(user_guess, correct_answer):
    if user_guess == correct_answer:
        return True
    else:
        return False
for question_num in range(len(question_bank)):

    print("\n************************")

    print(question_bank[question_num]["text"])

    
    for option in options[question_num]:
        print(option)

   
    user_guess = input("Enter your answer (A, B, C, or D): ").upper()

  
    correct_answer = question_bank[question_num]["answer"]

   
    if check_answer(user_guess, correct_answer):
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("Correct answer is:", correct_answer)


print("\n************************")
print("Quiz Finished!")
print("Your score is:", score, "/", len(question_bank))
print("Your percentile is :",score/len(question_bank)*100,"%")
print("************************")