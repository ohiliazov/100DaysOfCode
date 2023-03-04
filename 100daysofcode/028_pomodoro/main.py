import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
CHECKMARK = "✔"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

timer: str = ""
reps = 0


def reset_timer():
    global reps, timer

    if timer is None:
        return

    window.after_cancel(timer)

    reps = 0
    timer = None

    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")


def start_timer():
    global reps, timer

    if timer:
        return

    reps += 1
    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Short Break", fg=PINK)
    else:
        countdown(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)
    if reps % 2 == 0:
        checkmark_label.config(text=checkmark_label["text"] + CHECKMARK)


def countdown(total_seconds: int = 0):
    global timer

    minutes, seconds = divmod(int(total_seconds), 60)
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")

    if total_seconds > 0:
        timer = window.after(50, countdown, total_seconds - 1)
    else:
        timer = ""
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = tk.Label(
    text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 48, "bold"), width=11
)
timer_label.grid(column=1, row=0)

image = tk.PhotoImage(file="tomato.png")
canvas = tk.Canvas(
    width=200,
    height=224,
    bg=YELLOW,
    highlightthickness=0,
)
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(
    100,
    140,
    text="00:00",
    fill="white",
    font=(FONT_NAME, 24, "bold"),
)
canvas.grid(column=1, row=1)

start_button = tk.Button(
    text="Start",
    highlightthickness=0,
    command=start_timer,
)
start_button.grid(column=0, row=2)

reset_button = tk.Button(
    text="Reset",
    highlightthickness=0,
    command=reset_timer,
)
reset_button.grid(column=2, row=2)

checkmark_label = tk.Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 24, "bold"))
checkmark_label.grid(column=1, row=3)

window.mainloop()
