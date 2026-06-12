import os

# ==========================
# QUIZ QUESTIONS
# ==========================

questions = {
    "Easy": [
        {
            "question": "What does CPU stand for?",
            "answer": "central processing unit"
        },
        {
            "question": "What does RAM stand for?",
            "answer": "random access memory"
        }
    ],

    "Medium": [
        {
            "question": "Which language are we using?",
            "answer": "python"
        },
        {
            "question": "Which keyword is used to create a function in Python?",
            "answer": "def"
        }
    ],

    "Hard": [
        {
            "question": "Which data structure uses key-value pairs?",
            "answer": "dictionary"
        },
        {
            "question": "What file extension is used for Python files?",
            "answer": ".py"
        }
    ]
}

LEADERBOARD_FILE = "leaderboard.txt"


# ==========================
# FUNCTIONS
# ==========================

def show_leaderboard():
    print("\n===== LEADERBOARD =====")

    if not os.path.exists(LEADERBOARD_FILE):
        print("No scores yet!")
        return

    with open(LEADERBOARD_FILE, "r") as file:
        scores = file.readlines()

    if len(scores) == 0:
        print("No scores yet!")
        return

    for score in scores:
        print(score.strip())


def save_score(name, score):
    with open(LEADERBOARD_FILE, "a") as file:
        file.write(f"{name} - {score}\n")


def play_quiz():
    score = 0

    print("\nChoose Difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    choice = input("Enter choice (1-3): ")

    if choice == "1":
        selected = questions["Easy"]

    elif choice == "2":
        selected = questions["Medium"]

    elif choice == "3":
        selected = questions["Hard"]

    else:
        print("Invalid choice!")
        return

    print("\nStarting Quiz...\n")

    for q in selected:
        answer = input(q["question"] + " ")

        if answer.lower().strip() == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong!")
            print("Correct Answer:", q["answer"])
            print()

    print("===================")
    print("Quiz Finished!")
    print("Your Score:", score, "/", len(selected))
    print("===================")

    return score


# ==========================
# MAIN PROGRAM
# ==========================

print("===================================")
print("      PYTHON QUIZ CHALLENGE")
print("===================================")

name = input("Enter your name: ")

score = play_quiz()

save_score(name, score)

show_leaderboard()

print("\nThanks for playing!")