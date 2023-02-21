from data import get_question_data
from question_model import Question
from quiz_brain import QuizBrain

question_data = get_question_data()
question_bank = [
    Question(
        text=item["question"],
        answer=item["correct_answer"],
    )
    for item in question_data
]

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.finish()
