from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text , text = "00:00")
    timer_label.configure(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME,30,"bold"))
    reps = 0
    check_mark.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        timer_label.config(text="BREAK" , fg=RED ,bg=YELLOW)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        timer_label.config(text="BREAK", fg=PINK, bg=YELLOW)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        timer_label.config(text="WORK", fg=GREEN, bg=YELLOW)
        count_down(WORK_MIN * 60 )

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text , text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer;
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks =""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
            check_mark.configure(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# CREATE TIMER LABEL:
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME,30,"bold"))
timer_label.grid(row=0, column=1)

# CREATE TIMER ON THE TOMATO:
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0, )
tomate_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomate_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 32, "bold"), fill="white")
canvas.grid(row=1, column=1)

# CREATE START AND RESET BUTTONS:
start_btn = Button(text="Start", font=(FONT_NAME, 10, "bold"), highlightthickness=0 , bg=YELLOW , command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", font=(FONT_NAME, 10, "bold"), highlightthickness=0 , bg=YELLOW , command=reset_timer)
reset_btn.grid(row=2, column=2)

# CREATE DONE TEXTS:
check_mark = Label(fg=GREEN, bg=YELLOW, font=32)
check_mark.grid(row=3, column=1)

window.mainloop()
