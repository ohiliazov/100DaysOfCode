from tkinter import Button, Canvas, Label, PhotoImage, Tk

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.question_text = self.canvas.create_text(
            150,
            125,
            font=("Arial", 20, "italic"),
            text="Some question text",
            fill=THEME_COLOR,
            width=280,
        )

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.true_button = Button(
            image=true_image,
            bg=THEME_COLOR,
            highlightbackground=THEME_COLOR,
            activebackground=THEME_COLOR,
            highlightthickness=0,
            borderwidth=0,
            command=self.true_pressed,
        )
        self.false_button = Button(
            image=false_image,
            bg=THEME_COLOR,
            highlightbackground=THEME_COLOR,
            activebackground=THEME_COLOR,
            highlightthickness=0,
            borderwidth=0,
            command=self.false_pressed,
        )

        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")

            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
            self.true_button.config(state="active")
            self.false_button.config(state="active")
        else:
            self.score_label.config(text="")
            self.canvas.itemconfig(
                self.question_text,
                text=(
                    f"You've reached the end of the quiz.\n"
                    f"Your score is {self.quiz.score}/10!"
                ),
            )

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_correct: bool):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
