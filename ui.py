from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT_NAME = "Arial"
FONT_STYLE = "italic"

# just reference the flash card project, easy-peasy
# https://github.com/ashwinalexander/tkinter-flash-card/blob/master/main.py

class QuizInterface():

    # Learning:Set background color for the window, not the canvas
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.score = 0
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        # useful because it allows us to layer things on top
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Q text", width=280,fill=THEME_COLOR, font=(FONT_NAME, 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)

        # next configure the two images
        img_true = PhotoImage(file="images/true.png")
        img_false = PhotoImage(file="images/false.png")

        # position the true button on the grid
        self.btn_true = Button(image=img_true, highlightthickness=0, command=self.pick_true)
        self.btn_true.grid(row=2, column=0)

        # position the false button on the grid
        self.btn_false = Button(image=img_false, highlightthickness=0, command=self.pick_false)
        self.btn_false.grid(row=2, column=1)

        self.get_next_question()

        # like a never-ending while loop
        self.window.mainloop()

    def finish_game(self):
        self.canvas.itemconfig(self.question_text, text=f"Game Over. Your score is {self.quiz.score}")
        self.canvas.config(bg="yellow")
        self.btn_false.grid_forget()
        self.btn_true.grid_forget()
        print("game over")

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
           q_text = self.quiz.next_question()
           self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.finish_game()

    def pick_true(self):
        # increment score
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.update_canvas_color(self.quiz.check_answer("True"))

    def pick_false(self):
        # do not increment score
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.update_canvas_color(self.quiz.check_answer("False"))

    def update_canvas_color(self, is_correct: bool):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)











