import random
#Question to be asked
quiz_data = [
    {
        "question": "What is the symbol used to start a comment in python?",
        "options": ["A. *", "B. /", "C. #", "D. +"],
        "answer": "C"
    },
    {
        "question": "What is the correct file extension for Python files??",
        "options": ["A. .pt", "B. .pyt", "C. .py", "D. .python"],
        "answer": "C"
    },
    {
        "question": "What data type is the result of 5 + 3 in Python?",
        "options": ["A. int", "B. num", "C. digit", "D. str"],
        "answer": "A"
    },
    {
        "question": "How do you insert comments in Python Code?",
        "options": [ "A. // This is a comment", "B. /* This is a comment */", "C. # This is a comment", "D. -- This is a comment"],
        "answer": "C"
    },
    {
      "questions": " In Python, what does the len() function do?",
       "options": [ "A. Deletes a variable", "B. Returns the length of an object", "C. Counts integers only", "D. Prints the object"],
       "answer": "B"
    },
    {
        "question": "In Python, which keyword is used to define a function?",
        "options": ["A. define", "B. func", "C. def", "D. function"],
        "answer": "C"
    },
    {
        "question": "What is the output of the following code: `print(3 * 'Hello ')`?",
        "options": ["A. Hello Hello Hello Hello", "B. 9", "C. Hello Hello Hello", "D. Syntax Error"],
        "answer": "C"
    },
    {
        "question": "Which of the following is not a valid Python data type?",
        "options": ["A. set", "B. list", "C. array", "D. tuple"],
        "answer": "c"
    },
    {
        "question": "Which data type in Python is used to represent a sequence of characters?",
        "options": ["A. int", "B. float", "C. str", "D. list"],
        "answer": "C"
    },
    {
        "question": "Which of the following is used to define a block of code in Python?",
        "options": ["A. Braces[]", "B. Parentheses()", "C. Indentation", "D. Begin-End"],
        "answer": "C"
    },
    {
        "question": "What keyword is used to create a class in Python?",
        "options": ["A. class", "B. def", "C. define", "D. struct"],
        "answer": "A"
    },
    {
        "question": "In Python, which library is commonly used for data visualization?",
        "options": ["A. Seaborn", "B. Matplotlib ", "C. Matplotlib", "D. BeautifulSoup "],
        "answer": "C"
    },
    
    {
        "question": "Which of the following is not a valid Python data type?",
        "options": ["A. Python converts both to strings and returns '33'", "B. Python converts both to integers and returns 6", "C. Python raises a TypeError", "D. Python returns None"],
        "answer": "C"
    },
    {
        "question": "What happens when you try to add an integer and a string in Python, like `3 + '3'`?",
        "options": ["A. Python returns none" , "B. '33'", "C. TypeError", "D. '6'"],
        "answer": "B"
    },
    {
        "question": "Which built-in function returns the largest item in an iterable?",
        "options": ["A. biggest()", "B. max()", "C. large()", "D. maximum()"],
        "answer": "B"
    },
    {
        "question": "What is the purpose of the `if` statement in programming?",
        "options": ["A. To check if a condition is met before running code", "B. To declare a list of items", "C. To handle user input", "D. To import external files"],
        "answer": "A"
    },
    {
        "question": "GitHub is a VCS, what does that stand for?",
        "options": ["A. Version Compliance System", "B. Verified Control System ", "C. Version Control System", "D. Very Crazy System"],
        "answer": "C"
    },
    {
        "question": "What does CLONE do in GitHub?",
        "options": ["A. Add a file to a commit", "B. Stage changes with a message", "C. Copy a commit to repository", "D. Download a copy of a repository"],
        "answer": "D"
    },
    {
        "question": "Which of these is a valid variable name in Python?",
        "options": [ "A. 2cool", "B. cool_2", " C. cool-2", "D. @cool"],
        "answer": "B"
    },
    {
        "question": " Which one of these is a list in Python?",
        "options": [ "A. {1,2,3}", "B. (1,2,3)", "C. [1,2,3]", "D. 1,2,3"],
        "answer": "B"
    }
]
#displaying content
def ask_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    user_answer = input("Enter your answer (A,B,C,D): ").upper()
    if user_answer == question_data["answer"]:
        return True
    else:
        return False
#main body
if __name__=="__main__":
    score=0
    random.shuffle(quiz_data)
    for i in range(1,6):
        print(f'Question {i} of 5')
        if ask_question(quiz_data[i]):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {quiz_data[i]['answer']}.\n")

    print(f"You scored {score}/5.")
