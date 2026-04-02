import time
import json
numQuestions = 0
correctAnswers = 0

with open('Quiz App.json', 'r') as file:
    qAnswers = json.load(file)

for k in qAnswers.keys():
    numQuestions += 1
print(f"Welcome to the Quiz App!\n\nAnswer the following {numQuestions} questions:\n----------------------------------")
#if the json file is edited the quiz will still work as it is based on what is in the file
for key,value in qAnswers.items():
    #loop to ensure that the user enters a valid answer like 'c' or 'python' even if not correct
    while True:
        #prints the question number and the guestion stored in the key
        print(f"Question {key}:\n{value["question"]}")
        for option in range(0,(len(value["options"])),2):
            print(f"{value["options"][option]}. {value["options"][option+1]}")
        #takes the users answer
        correct = input("Your Answer: ")
        #transforms the current option list to be completely lower case, so it still prints properly to the user
        lowList = [opt.lower() for opt in value["options"]]
        lowAnswer = value["answer"]
        lowAnswer = lowAnswer.lower()
        #if the answer is 'Paris' the user will not be told to pick from available options if they type 'paris'
        #if they pick an invalid answer they are put in a loop until they pick a valid one
        if correct.lower() not in lowList:
           print("Pick from the options available.\n")
           time.sleep(0.5)
        #if they pick the right letter 'C' or the right answer 'BiLl gATes' they are awarded with a 'Correct!'
        elif correct.lower() == value["letter"] or correct.lower() == lowAnswer:
            print("Correct!")
            correctAnswers += 1
            break
        else:
            #if they pick a valid but wrong answer
            #when print the correct answer it may not always be as simple as putting it in titlecase 
            #if the correct answer was "Python" title case works but not if the correct answer is "HTML"
            #to fix this we have two different answer values for printing and for working with
            print(f"Wrong.\nCorrect answer: {value["letter"]}. {value["answer"]}")
            time.sleep(0.5)
            break
    print("----------------------------------")
    time.sleep(0.5)
print("Quiz completed!\n----------------------------------")
print(f"Total Questions: {numQuestions}\nCorrect Answers: {correctAnswers}\nWrong Answers: {numQuestions-correctAnswers}\nScore: {correctAnswers}/{numQuestions}")
percentage = (correctAnswers/numQuestions)*100
if correctAnswers == 0:
    print("Percentage: 0%")
else:
    print(f"Percentage: {percentage:.0f}%")
print("----------------------------------")
if percentage == 100:
    print("Excellent Performance.")
elif percentage>50:
    print("Good try!")
else:
    print("Better luck next time.")
