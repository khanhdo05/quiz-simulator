from string import ascii_lowercase

# Dictionary of questions with alternatives, the first element of the alternatives is the correct answer.
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

for num, (question, alternatives) in enumerate(QUESTIONS.items(), start=1):
    print(f"\nQuestion {num}:") #\n for new line
    print(f"{question}?")

    correct_answer = alternatives[0]
    sorted_alternatives = sorted(alternatives)

    labeled_alternatives = dict(zip(ascii_lowercase, sorted_alternatives))
    for label, alternative in labeled_alternatives.items():
        print(f"    ({label}) {alternative}")

    answer_label = input("\nChoice: ")
    answer_label = answer_label.lower()
    answer = labeled_alternatives.get(answer_label)
    if answer == correct_answer:
        print("⭐ Ding ding! Correct! ⭐")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}.") #!r put the {} in ''