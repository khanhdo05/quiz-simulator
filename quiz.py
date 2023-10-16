QUESTIONS = [
    ("What is the color for: Stop, yield, or do what is shown on the sign", "red"),
    ("What is the color for: Direction. Indicates where a place is, or how far a place is from where you are", "green"),
    ("What is the color for: Regulatory. Provides information regarding enforceable laws and ordinances", "white")
]

for question, correct_answer in QUESTIONS:
    answer = input(f"{question} ? ")
    if answer.lower() == correct_answer:
        print("Ding ding! Correct!")
    else:
        print(f"The answer if {correct_answer}, not {answer}.")