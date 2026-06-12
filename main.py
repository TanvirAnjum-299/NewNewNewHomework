class Quiz:
    def __init__(self, questions):
        # Constructor initializes questions and score
        self.questions = questions
        self.score = 0

    def ask_question(self, question, answer):
        # Function to ask a question and check answer
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            print("✅ Correct!")
            self.score += 1
        else:
            print("❌ Wrong! The correct answer was:", answer)

    def start(self):
        # Loop through all questions
        for q, a in self.questions:
            self.ask_question(q, a)
        self.final_score()

    def final_score(self):
        # Conditional feedback based on score
        print(f"\nYour final score is {self.score}/{len(self.questions)}")
        if self.score == len(self.questions):
            print("🎉 Excellent! Full marks!")
        elif self.score >= len(self.questions) // 2:
            print("👍 Good job, keep practicing!")
        else:
            print("📚 Needs more practice, don’t give up!")

# -------------------------------
# Example Questions (you can add more)
questions = [
    ("What is the capital of Bangladesh?", "Dhaka"),
    ("Which keyword is used to define a function in Python?", "def"),
    ("What does OOP stand for?", "Object Oriented Programming"),
    ("Which loop is used when you know the number of iterations?", "for"),
    ("Which statement is used for decision making in Python?", "if")
]

# Create Quiz object and start
quiz = Quiz(questions)
quiz.start()
