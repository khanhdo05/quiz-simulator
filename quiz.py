import random
from string import ascii_lowercase

NUM_QUESTIONS_PER_QUIZ = 25
# Dictionary of questions with alternatives, the first element of the alternatives is the correct answer.
QUESTIONS = {
    "When preparing to make a left turn from a two-way street, you should drive" : [
        "Close to the center line", 
        "Close to the right hand side of the road", 
        "On the left of the center line"
    ],
    "By looking ahead, to the sides of your vehicle and behind your vehicle as you drive, you will" : [
        "See potential problems and become better prepared to react", 
        "Cause neck pain", 
        "Lose points on your driving record"
    ],
    "A flashing yellow light means" : [
        "Slow down and proceed with caution",
        "Stop and wait for directions from a police officer", 
        "Speed up"
    ],
    "When driving behind another vehicle on an entrance to a freeway, you should" : [
        "Be prepared for the other vehicle to slow down",
        "Be prepared to enter the same gap of traffic as the other vehicle",
        "Not go faster than 20 mph"
    ],
    "On an undivided highway when an emergency vehicle approaches with its siren and/or flashing lights on, you should" : [
        "Pull to the right and stop",
        "Drive slowly until it has passed",
        "Speed up to clear traffic"
    ],
    "If the rear of your vehicle is skidding to the left, you should" : [
        "Turn your steering wheel to the left to correct the skid",
        "Not turn your steering wheel until you are through skidding",
        "Turn your steering wheel to the right to correct the skid"
    ],
    "When approaching a stopped vehicle, such as a police car, tow truck, utility or maintenance vehicle, that is parked along the road and displaying flashing lights, what should you do" : [
        "Change lanes if you safely can and slow down to a reasonable and safe speed as you pass",
        "Stop abruptly",
        "Continue as usual"
    ],
    "According to the Iowa Implied Consent Law for both resident and nonresident drivers" : [
        "Both of the options are true",
        "An arrested driver may be asked to submit to a chemical test to determine the alcohol content in his/her blood.",
        "Refusal to submit to chemical testing will result in the driver's driving privileges being withdrawn."
    ],
    "You see a school bus with flashing amber (yellow) lights. What is the bus driver doing" : [
        "Signaling to other motorists that the bus will soon be stopping to load or unload school children",
        "Changing gears",
        "Preparing to make a turn"
    ],
    "Which of the following is a safe backing technique" : [
        "Accelerate gently and smoothly while looking carefully behind you",
        "Look forward out through the windshield",
        "Hold the steering wheel underhanded"
    ],
    "What should you do as you approach a curve in the road" : [
        "Reduce your speed before you enter the curve",
        "Shift your weight behind the wheel",
        "Put on your four-way flashers"
    ],
    "If you are on a two-lane highway when meeting an oncoming school bus with its amber (yellow) warning lights flashing, you must" : [
        "Slow to 20 mph and prepare to stop",
        "Continue as usual",
        "Stop at least 10 feet from the front of the bus"
    ],
    "You are driving on a road that has two or more lanes in each direction. You meet a school bus traveling the opposite direction that is stopped with flashing red lights. Are you required to stop" : [
        "No, when you are approaching a stopped school bus from the opposite direction on a road that has two or more lanes in each direction, you are not required to stop and may continue carefully. This is the only time you can pass a school bus that displays flashing red lights.",
        "Yes, you should always stop for a school bus that displays red flashing lights"
    ],
    "Because there is often slow-moving traffic on county highways, you should" : [
        "Be ready to change your speed to the speed of traffic",
        "Stay in the left lane and drive at the speed limit",
        "Pass slow-moving vehicles on curves if they are slowing down"
    ],
    "When passing a vehicle, you should return to your lane when" : [
        "You can see both its headlights in your rearview mirror",
        "You have cleared the front bumper of the passed vehicle",
        "You are 50 feet in front of the passed vehicle"
    ],
    "You are approaching an intersection and see these pavement markings. What do these pavement markings tell you" : [
        "You may make a right turn only from the right lane",
        "The two lanes will merge into one",
        "The vehicle in the right lane must turn right"
    ],
    "Which of the below are common factors contributing to traffic crashes" : [
        "Exceeding the posted speed limit and driving too fast for conditions or circumstances",
        "Getting adequate rest and staying alert",
        "Scanning the environment and staying focused on the driving task"
    ],
    "If you must park your vehicle in an area not usually used for parking" : [
        "Make sure your vehicle is visible to drivers approaching from either direction",
        "Park with your back-up lights on",
        "Park 5 feet from the curb"
    ],
    "Which is the correct sequence of events as a school bus driver prepares to stop to load or unload children" : [
        "Amber lights flash at the top of the bus, the bus stops as red lights flash, a stop arm goes out and the door opens for the school children",
        "The bus driver activates red flashing lights at the top of the bus, and then activates amber flashing lights when the children are unloaded or seated",
        "The bus driver may do any sequence he or she desires"
    ],
    "Which of the following statements are true about safe following distance between your vehicle and the vehicle in front of you?" : [
        "All options",
        "A two-second following distance may be sufficient in normal conditions for an experienced driver",
        "An inexperienced or beginning driver should maintain at least a three-second following distance under normal driving conditions",
        "At speeds of 40 mph, a four- to five-second following distance is recommended. When road conditions are slippery or the vehicle in front of you blocks your view, a following distance of six or more seconds is recommended."
    ],
    "Passing is prohibited when" : [
        "You are within 100 feet of an intersection or railroad crossing",
        "The vehicle you are following has a slow-moving vehicle symbol",
        "You would be required to pass to the right of a left turning vehicle"
    ],
    "When you are merging onto the freeway or interstate, you should be driving" : [
        "At or near the same speed as the traffic on the freeway or interstate",
        "5 to 10 mph slower than the traffic on the freeway or interstate",
        "The posted speed limit for traffic on the freeway or interstate"
    ],
    "In speed zones of 45 mph or less, you must signal your turn continuously during the last ______feet before turning" : [
        "100 ft",
        "200 ft",
        "300 ft"
    ],
    "In speed zones of 45 mph or more, you must signal your turn continuously during the last ______feet before turning" : [
        "300 ft",
        "200 ft",
        "100 ft"
    ],
    "You should always travel" : [
        "According to road and weather conditions",
        "At the speed of vehicles in front of you",
        "At the speed limit"
    ],
    "When it is raining, you should be most careful when turning or stopping" : [
        "During the first half hour of rain",
        "A half hour after it stops raining",
        "After it has been raining all day"
    ],
    "You are traveling on a two- or three-lane road and meet a stopped school bus with its red lights flashing. You must" : [
        "Stop and remain stopped until the red lights stop flashing and the stop arm is withdrawn",
        "Stop and proceed after a few seconds",
        "Stop only if children are crossing the roadway"
    ],
    "Broken yellow lines (dashes) are used on streets and highways to" : [
        ""
    ],
    "Unless a sign is posted, you may turn right at a red light if" : [
        ""
    ],
    "Before making a turn, you should" : [
        ""
    ]
}

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