from tkinter import *
from random import randint, choice, shuffle
import pyperclip
from tkinter import messagebox
import json


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
    # create dictionary for our json
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have not left any filed empty ")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # update old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_enter.delete(0, END)
            password_enter.delete(0, END)


# ----------------------------------------- Find password ------------------------------
def find_password():
    website = website_enter.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="not data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"no detail for {website} exist.")


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
website_enter = Entry(width=44)
website_enter.grid(row=1, column=1)

Email_enter = Entry(width=63)
Email_enter.grid(row=2, column=1, columnspan=2)

password_enter = Entry(width=44)
password_enter.grid(row=3, column=1)

# button
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)

generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=54, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
