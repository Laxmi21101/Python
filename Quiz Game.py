import random

# Sample quiz questions and answers
quiz_questions = [
    {
        "question": "What is the capital of Uttar Pradesh?",
        "choices": ["A) London", "B) Lucknow", "C) Paris", "D) Rome"],
        "correct_answer": "B) Lucknow"
    },
    {
        "question": "What is the national river of India?",
        "choices": ["A) Indus", "B) Ganga", "C) Yumnana", "D) Godavari"],
        "correct_answer": "B) Ganga"
    },
    {
        "question": "What is the largest mammal in the world?",
        "choices": ["A) African Elephant", "B) Blue Whale", "C) Giraffe", "D) Hippopotamus"],
        "correct_answer": "B) Blue Whale"
    }
]

def display_question(question_data):
    print(question_data["question"])
    for choice in question_data["choices"]:
        print(choice)
    user_answer = input("Your answer: ")
    return user_answer

def evaluate_answer(user_answer, correct_answer):
    return user_answer.strip().lower() == correct_answer.lower()

def play_quiz(questions):
    score = 0
    total_questions = len(questions)
    
    for question in questions:
        print("=" * 40)
        user_answer = display_question(question)
        
        if evaluate_answer(user_answer, question["correct_answer"].split(")")[1]):
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {question['correct_answer']}")
    
    print("=" * 40)
    print("Quiz completed!")
    print(f"Your score: {score}/{total_questions}")
    
    if score == total_questions:
        print("Congratulations! You got all the questions right!")
    elif score >= total_questions / 2:
        print("Well done! You did a good job!")
    else:
        print("Keep practicing to improve your score.")

def main():
    print("Welcome to the Quiz Game!")
    print("Test your knowledge and have fun!\n")
    
    play_again = "yes"
    while play_again.lower() == "yes":
        random.shuffle(quiz_questions)
        play_quiz(quiz_questions)
        
        play_again = input("Do you want to play again? (yes/no): ")

    print("Thank you for playing!")

if __name__ == "__main__":
    main()
