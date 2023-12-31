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

# Deals with general parameters, not specific constants bound above -> doesn't depend on global variables
def prepare_questions(path, num_questions):
    questions = tomllib.loads(path.read_text())["questions"]
    num_questions = min(num_questions, len(questions))
    return random.sample(questions, k=num_questions)

# Handles user interaction
def get_answers(question, alternatives, num_choices=1):
    print(f"{question}❓")

    # Print alternatives labeled by a, b, c,... 
    labeled_alternatives = dict(
        zip(ascii_lowercase, alternatives)
    )
    for label, alternative in labeled_alternatives.items():
        print(f"    ({label}) {alternative}")

    # Handles when to display Choice or Choices (choose how many)
    while True:

        plural_s = "" if num_choices == 1 else f"s (choose {num_choices})" # If num_choice is 1, add nothing, else, add how many choices need to choose
        answer = input(f"\nChoice{plural_s}: ")
        answers = set(answer.replace(",", " ").split()) # Create a set of answers, replacing , with space and then split that string by space

        # Handles invalid answer
        if len(answers) != num_choices:
            plural_s = "" if num_choices == 1 else f"s, separated by comma"
            print(f"Please answer {num_choices} alternative{plural_s}")
            continue # Skip the remaining code inside a loop for the current iteration only

        invalid = [ans for ans in answers if ans not in labeled_alternatives]
        if invalid:
            print(
                f"{invalid!r} is an invalid choice. "
                f"Please use one of the following: {', '.join(labeled_alternatives)}"
            )
            continue

        return [labeled_alternatives[answer] for answer in answers]

# Check if answer is corect or not, if correct, return 1, so later can count how many correct answers
def ask_question(question):
    correct_answers = question["answers"]
    alternatives = question["answers"] + question["alternatives"]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answers = get_answers(
        question=question["question"], 
        alternatives=ordered_alternatives,
        num_choices=len(correct_answers),
    ) 

    if set(answers) == set(correct_answers):
        print("⭐ Ding ding! Correct! ⭐")
        return 1
    else:
        is_or_are = " is" if len(correct_answers) == 1 else "s are"
        print("\n- ".join([f"No. The correct answer{is_or_are}:"] + correct_answers))
        return 0

def run_quiz():
    questions = prepare_questions(
        QUESTIONS_PATH, num_questions=NUM_QUESTIONS_PER_QUIZ
    )

    num_correct = 0
    for num, question in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question)

    print(f"\nYou got {num_correct} correct out of {num} questions")

# Protect run_quiz call with an if __name__ == "__main__" test
if __name__ == "__main__":
    run_quiz()