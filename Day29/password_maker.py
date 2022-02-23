from tkinter import *
from random import randint, choice, shuffle
import pyperclip


# -------------------------------------- password generator ---------------------------

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '8', '9']
    symbol = ['!', '$', '#', '%', '^', '&', '*', '(', ')']
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbol = [choice(symbol) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbol
    shuffle(password_list)

    password = "".join(password_list)
    password_enter.insert(0, password)
    pyperclip.copy(password)


# ------------------------------------- save password -----------------------------------
def save():
    website = website_enter.get()
    email = Email_enter.get()
    password = password_enter.get()

    with open("file.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")
        website_enter.delete(0, END)
        password_enter.delete(0, END)


# ----------------------------------------- UI -----------------------------------------
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=256, height=256)
key_img = PhotoImage(file="logo.png")
canvas.create_image(130, 130, image=key_img)
canvas.grid(column=1, row=0)

# Labels
label_website = Label(text="website")
label_website.grid(column=0, row=1)

label_Email = Label(text="Email/Username")
label_Email.grid(column=0, row=2)

label_Password = Label(text="Password")
label_Password.grid(column=0, row=3)

# Enters
website_enter = Entry(width=63)
website_enter.grid(row=1, column=1, columnspan=2)

Email_enter = Entry(width=63)
Email_enter.grid(row=2, column=1, columnspan=2)

password_enter = Entry(width=44)
password_enter.grid(row=3, column=1)

# button
generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=54, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
