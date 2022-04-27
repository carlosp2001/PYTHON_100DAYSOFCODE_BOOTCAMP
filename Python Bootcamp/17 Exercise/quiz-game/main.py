from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question_info in question_data:
    question_bank.append(Question(text=question_info['text'], answer=question_info['answer']))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz")
print(f"You're final score was: {quiz.score}/{len(question_bank)}")
