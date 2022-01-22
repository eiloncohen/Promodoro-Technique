from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WHITE = "#ffffff"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global reps, correct_mark_label, timer_label
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(timer)
    reps = 0
    correct_mark_label.configure(text="", font=(FONT_NAME, 14, "bold"), fg=GREEN, bg=YELLOW)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def add_vi_mark(append):
    global correct_mark_label
    if append:
        text = correct_mark_label.cget("text") + append
        correct_mark_label.configure(text=text, font=(FONT_NAME, 14, "bold"), fg=GREEN, bg=YELLOW)



def start_timer():
    global reps, correct_mark_label
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 8:
        text = "Long Break"
        count_down(long_break_sec)
        timer_label.config(text=text, fg=RED)
        reps = 0

    elif reps % 2 == 1:
        if reps == 1:
            correct_mark_label.config(text="")
        text = "Time To Work"
        count_down(work_sec)
        timer_label.config(text=text, fg=GREEN)
    else:
        text = "Short Break"
        count_down(short_break_sec)
        timer_label.config(text=text, fg=PINK)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pormodoro")
window.config(padx=200, pady=100, bg=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer_label, timer
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = "0"+str(minutes)
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        add_vi_mark("✓")


timer_label = Label(text="Timer", font=(FONT_NAME,35,"bold"), fg=GREEN ,bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=1)


start_btn = Button(text="Start", bg=PINK, fg=WHITE, relief='flat', width=10, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", bg=PINK, fg=WHITE, relief='flat', width=10, command=reset)
reset_btn.grid(column=2, row=2)


correct_mark_label = Label(text="",  font=(FONT_NAME, 14, "bold"), fg=GREEN, bg=YELLOW)
correct_mark_label.grid(column=1, row=3)


window.mainloop()


