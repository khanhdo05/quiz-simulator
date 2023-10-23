# quiz.py

import random
from string import ascii_lowercase
import pathlib # Use pathlib to handles the path to questions.toml
try: # Wrapping import in a try-except statement
    import tomllib # First try to import tomllib (if using Python 3.11)
except ModuleNotFoundError: # If fails
    import tomli as tomllib # Try to import tomli but renames as tomllib

NUM_QUESTIONS_PER_QUIZ = 25
QUESTIONS_PATH = pathlib.Path(__file__).parent / "questions.toml"
QUESTIONS = tomllib.loads(QUESTIONS_PATH.read_text())

# Deals with general parameters, not specific constants bound above -> doesn't depend on global variables
def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)

# Handles user interaction
def get_answer(question, alternatives):
    print(f"{question}❓")

    # Print alternatives labeled by a, b, c,... 
    labeled_alternatives = dict(
        zip(ascii_lowercase, alternatives)
    )
    for label, alternative in labeled_alternatives.items():
        print(f"    ({label}) {alternative}")

    # Ask for user's input of alternative label, check if it's a valid one or not
    while (answer_label := input("\nChoice: ").lower()) not in labeled_alternatives: # := to assign variable within expressions
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    # get_answer takes in 2 parameters, a question and its alternative options and return the alternative that user chose
    return labeled_alternatives[answer_label]

# Check if answer is corect or not, if correct, return 1, so later can count how many correct answers
def ask_question(question, alternatives):
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = get_answer(question, ordered_alternatives) # ask_question implements get_answer within its body
    if answer == correct_answer:
        print("⭐ Ding ding! Correct! ⭐")
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}.") #!r put the {} in ''
        return 0

# Combine every helper funcs together
def run_quiz():
    questions = prepare_questions(QUESTIONS, NUM_QUESTIONS_PER_QUIZ)

    num_correct = 0
    for num, (question, alternatives) in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question, alternatives)

    print(f"You've got {num_correct} correct answers out of {num} questions!")

# Protect run_quiz call with an if __name__ == "__main__" test
if __name__ == "__main__":
    run_quiz()