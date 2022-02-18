from tkinter import *

window = Tk()

window.title("my first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=50)


def buttom_click():
    miles = float(input.get())
    km = miles * 1.609
    label_3.config(text=km)


input = Entry(width=10)
input.grid(column=1, row=0)

label_1 = Label(text="Miles", font=("Arial", 18))
label_1.grid(column=2, row=0)

label_2 = Label(text="is equal to", font=("Arial", 18))
label_2.grid(column=0, row=1)

label_3 = Label(text="0", font=("Arial", 18))
label_3.grid(column=1, row=1)

label_4 = Label(text="Km", font=("Arial", 18))
label_4.grid(column=2, row=1)

bottom = Button(width=10, text="calculate", command=buttom_click)
bottom.grid(column=1, row=2)


window.mainloop()
