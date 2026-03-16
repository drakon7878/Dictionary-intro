import random

questions = (" Which country has the most natural lakes? ",
                    "What is the only continent that lies in all four hemispheres?",
                    "What is the smallest country in the world by land area?",
                    "What is the hardest natural substance on Earth?",
                    "What does HTTP stand for in a website address?"
)

answers = ("Canada",
                "Africa",
                "Vatican City.",
                "Diamond",
                "HyperText Transfer Protocol."
)

for i in range(5):
    correct = 0 
    print("Q"+str(i+1)+"."+questions[i])
    answerGiven = input("Type your answer here-->")
    if answerGiven == answers[i]:
        print("Correct! the answer is "+ answers[i]+" Here is your next question\n")
        correct+=1
    else:
        print("Incorrect, the answer was actually", answers[i]+ ". Here is your next question\n")

if correct == 5:
    print("Brilliant! you have gotten all the questions correct")


