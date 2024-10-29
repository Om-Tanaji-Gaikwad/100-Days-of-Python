# The Question Quiz with OOP

from day_17_data import question_data
from day_17_question_model import Question
from day_17_quiz_brain import QuizBrain

question_bank = []
for questions in question_data:
    question_text=questions["text"]
    question_answer=questions["answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)
while(quiz.still_has_que_left()):
    quiz.next_question()

print("\n\nThe quiz has completed.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
