from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quizbrain:QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quiz game")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas()
        self.canvas.config(height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125, text="something", width=280, font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.label = Label(text="score = 0",fg="white")
        self.label.config(background=THEME_COLOR)
        self.label.grid(column=1, row=0)

        right_image = PhotoImage(file="true.png")
        wrong_image = PhotoImage(file="false.png")
        self.right_button = Button(image=right_image, highlightthickness=0, command=self.true_pressed)
        self.right_button.grid(row=2, column=0)

        self.wrong_button = Button(image=wrong_image, highlightthickness=0,command=self.false_pressed)
        self.wrong_button.grid(row=2, column=1)
        self.canvas.config(bg="white")
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You have reached the end of the game")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        answer = self.quiz.check_answer("True")
        self.give_feedback(answer)

    def false_pressed(self):
        answer = self.quiz.check_answer("False")
        self.give_feedback(answer)

    def give_feedback(self,answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



