# Quiz Questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["a) Paris", "b) Rome", "c) Berlin", "d) Madrid"],
        "answer": "a"
    },
    {
        "question": "Which language is used to write Python code?",
        "options": ["a) HTML", "b) Python", "c) C++", "d) Java"],
        "answer": "b"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["a) Central Programming Unit", "b) Central Processing Unit", "c) Computer Power Unit", "d) Control Processing Unit"],
        "answer": "b"
    }
]

# Quiz logic inside a function
def run_quiz():
    score = 0

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        # Input with error handling
        while True:
            try:
                user_answer = input("Your answer (a/b/c/d): ").lower()
                if user_answer not in ['a', 'b', 'c', 'd']:
                    raise ValueError("Invalid option")  # Force error if input is not one of the options
                break  # Exit loop if input is valid
            except ValueError as e:
                print("Please enter a valid option (a, b, c, or d).")

        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {q['answer']}")

    print(f"\nYour final score is {score}/{len(questions)}")


# Game loop so player can replay
while True:
    run_quiz()

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing, peace out!")
        break