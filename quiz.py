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
QUESTIONS = tomllib.loads(QUESTIONS_PATH.read_text()) # read_text() to read toml file as a text string and then loads() to parse that string into a dict

# Deals with general parameters, not specific constants bound above -> doesn't depend on global variables
def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)

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