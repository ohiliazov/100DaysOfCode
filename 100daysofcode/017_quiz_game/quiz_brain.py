from html import unescape
from typing import List

from question_model import Question


class QuizBrain:
    def __init__(self, question_list: List[Question]):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def check_answer(self, answer: str, correct_answer: str):
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{len(self.question_list)}")
        print()

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(
            f"Q.{self.question_number}: {unescape(current_question.text)} (True/False): "
        )
        self.check_answer(answer, current_question.answer)

    def finish(self):
        print("You've completed the quiz.")
        print(f"Your final score is: {self.score}/{len(self.question_list)}")
