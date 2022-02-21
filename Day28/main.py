from tkinter import *
import math
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
#------------------------------timer reset----------------------------------------
def timer_reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "00:00")
    my_label.config(text="timer")
    label_2.config(text="")


# -----------------------------timer mechanism-------------------------------------
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        my_label.config(text="break", fg="#FC4F4F")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        my_label.config(text="break", fg="#FC4F4F")
    else:
        count_down(work_sec)
        my_label.config(text="work", fg="#65C18C")

# ---------------------------count down mechanism----------------------------------
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        label_2.config(text=marks)


# ----------------------------------- UI --------------------------------------------

window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg="#EFDAD7")

my_label = Label(text="Timer", font=("Arial", 32), bg="#EFDAD7", fg="#65C18C")
my_label.grid(column=1, row=0)

canvas = Canvas(width=256, height=257, bg="#EFDAD7", highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(128, 128, image=tomato_img)
timer_text = canvas.create_text(128, 134, text="00:00", fill="white", font=("Arial", 32, "bold"))
canvas.grid(column=1, row=1)

button_1 = Button(text="Start", command=start_timer)
button_1.grid(column=0, row=2)

button_2 = Button(text="Reset", command=timer_reset)
button_2.grid(column=2, row=2)

label_2 = Label(text="", font=(20), bg="#EFDAD7", fg="#65C18C")
label_2.grid(column=1, row=3)

window.mainloop()
