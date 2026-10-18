QuestionData = []

question_1 = {"question":"What is the correct file extension for Python?",
                 "options":["A → .py","B → .python","C → .pt","D → .p"],
                 "answer":"A"}
question_2 = {"question":"Which keyword is used to create a function in Python?",
              "options":["A → function","B → def","C → fun","D → create"],
              "answer":"B"}
question_3 = {"question":"Which data type stores multiple items in an ordered collection?",
              "options":["A → list","B → int","C → bool","D → float"],
              "answer":"A"}
question_4 = {"question":"Which symbol is used for comments in Python?",
              "options":['A → //','B → /*','C → #', 'D → --'],
              "answer": "C"}

QuestionData.append(question_1)
QuestionData.append(question_2)
QuestionData.append(question_3)
QuestionData.append(question_4)

def ask_question(x):
    for option in x["options"]:
        print(option)
    user_answer = input("Enter Your Answer:")
    print(user_answer)
    if user_answer.lower() == x["answer"].lower():
        print("Your Answer is Correct.")
        return 1
    else:
        print("your Answer is not Correct.")
        return 0
def run_quiz():
    score  = 0
    for x in QuestionData:
        print(x["question"])
        score+=ask_question(x)
    return score
def show_result(score):
    totalQuestion= len(QuestionData)
    percentage = score / totalQuestion*100
    print("Final Score is:",score,"/",totalQuestion)
    print("The percentage is:",percentage)

score = run_quiz()  
show_result(score)