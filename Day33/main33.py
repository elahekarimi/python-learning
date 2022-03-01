from tkinter import *
import requests

window = Tk()
window.config(padx=50, pady=50)
window.title("kanye says ...")

def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)

canvas = Canvas()
canvas.config(width=300, height=414)
background_image = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_image)
quote_text = canvas.create_text(150, 207, text="kanye quote goes here", width=250, font="Arial")
canvas.grid(row=0, column=0)

kanye_image = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_image, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()