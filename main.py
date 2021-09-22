import math
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
reps = 0
timer = None

def click2():
    global reps

    window.after_cancel(timer)
    canvas.itemconfig(text_new,text ="00:00" )
    title1.config(text = '')
    title.config(text = "Timer",fg=GREEN)
    reps = 0

def click1():
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title.config(text = "Break:)", fg = GREEN)
        count_down(long_break_sec)

    elif reps % 2 == 0:
        title.config(text="Break:)",fg =PINK)
        count_down(short_break_sec)
    else:
        title.config(text = "Work:(",fg=RED)
        count_down(work_sec)




def count_down(count):
    global timer
    count_min = math.floor(count/ 60)
    count_sec = count % 60
    #
    # if count_sec == 0:
    #     count_sec = "00"
    if count_sec <10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(text_new, text = f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        click1()
        marks  = ""
        for i in range(math.floor(reps/2)):
            marks += "✔"
        title1.config(text = marks)





title = Label(text="timer ", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
title.grid(column=1, row=0)


button1 = Button(text='start', command=click1,highlightthickness=0)
button1.grid(column = 0, row = 3)

button2 = Button(text='stop', command=click2,highlightthickness=0)
button2.grid(column = 3, row = 3)

title1 = Label(text="", bg=YELLOW, fg=GREEN, font=("Arial", 20, "bold"))
title1.grid(column=1, row=4)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
text_new = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=1, row=1)



window.mainloop()
