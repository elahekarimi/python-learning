from tkinter import *

window = Tk()

window.title("my first GUI program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

my_label = Label(text="im a label", font=("Arial", 24))
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)


def button_clicked():
    # print("Got click")
    my_label.config(text=input.get())

button = Button(text="click me", command=button_clicked)
button.grid(column=2, row=0)

button = Button(text="click me", command=button_clicked)
button.grid(column=1, row=1)

input = Entry(width=10)
input.grid(column=3, row=2)
# print(input.get())

window.mainloop()
