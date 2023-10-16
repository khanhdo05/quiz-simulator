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

num_correct = 0

# System explanation: A for loop to initerate over the dictionary QUESTIONS with num as index (start=1) to label each
# question. Display the Question No. and the question itself. And then create a dictionary of the ascii_lowercase as
# key, and the sorted_alternatives as values. 
for num, (question, alternatives) in enumerate(QUESTIONS.items(), start=1):
    print(f"\nQuestion {num}:") #\n for new line
    print(f"{question}❓")

    correct_answer = alternatives[0]
    sorted_alternatives = sorted(alternatives)

    labeled_alternatives = dict(zip(ascii_lowercase, sorted_alternatives))
    for label, alternative in labeled_alternatives.items():
        print(f"    ({label}) {alternative}")

    answer_label = input("\nChoice: ")
    answer_label = answer_label.lower()
    answer = labeled_alternatives.get(answer_label)
    if answer == correct_answer:
        num_correct += 1 # Increase by 1 if answer correctly
        print("⭐ Ding ding! Correct! ⭐")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}.") #!r put the {} in ''

print(f"You've got {num_correct} correct answers!")