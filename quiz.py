from string import ascii_lowercase

QUESTIONS = {
    "What is the color for: Stop, yield, or do what is shown on the sign" : [
        "red", "white", "green", "yellow"
    ],
    "What is the color for: Direction. Indicates where a place is, or how far a place is from where you are" : [
        "green", "white", "red", "yellow"
    ],
    "What is the color for: Regulatory. Provides information regarding enforceable laws and ordinances" : [
        "white", "red", "green", "yellow"
    ]
}

for question, alternatives in QUESTIONS.items():
    correct_answer = alternatives[0]
    sorted_alternatives = sorted(alternatives)
    for option, alternative in enumerate(sorted_alternatives):
        print(f"({option}) {alternative}")

    answer_option = int(input(f"{question}? "))
    answer = sorted_alternatives[answer_option]
    if answer.lower() == correct_answer:
        print("Ding ding! Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}.") #!r put the {} in ''