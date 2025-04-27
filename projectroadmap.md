Project Roadmap: Python Quiz
1. Plan the Basics
Goal: A console-based quiz where users answer multiple-choice questions on Python knowledge.

Decide on the number of questions: We decided as a group that we would develop 15-20 questions. (THIS IS DONE)

Questions format: Each has a question, 4 options, and a correct answer.

Scoring: +1 for correct, 0 for wrong. 17-20 points = Excellent. 12-17 points = Good. 7-12 points = Needs Improvement. 0-7 points = Fail

2. Organize Your Data
Task: Store quiz questions in a structured format.

To Do:

Use a list of dictionaries:

python
Copy
Edit
questions = [
    {
        "question": "What is the output of print(2**3)?",
        "options": ["5", "6", "8", "9"],
        "answer": "8" },
    # more questions...]
 3. Build the Quiz Logic
Task: Display questions and collect user input.

To Do:

Use a loop to go through each question.

Show question and options.

Get and validate user input (a, b, c, or d).

Check if the answer is correct.

Keep score.

 4. Add Feedback and Score
Task: Show correct/incorrect and final result.

To Do:

Show feedback after each question.

Display the final score at the end.

 5. Clean Up the User Interface
Task: Improve readability.

To Do:

Add line breaks.

Number the questions.

Clear or separate each question visually.
 6. (Optional) Add Features
Here’s where you can get creative:

Timer for each question.

Load questions from a .json or .csv file.

Randomize question order.

Show explanations after answers.

Add categories (e.g., Basics, Functions, Loops).

Build a GUI using Tkinter or a web version with Flask.


