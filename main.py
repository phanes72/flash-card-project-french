from tkinter import *
import pandas as pd
import random

data = pd.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = random.choice(to_learn)

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_title = canvas.create_text(400, 150, text="English", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text=current_card["English"], font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0)
known_button.grid(row=1, column=1)


def flip_card():
    canvas.config(bg="white", highlightthickness=0)
    canvas.itemconfig(card_title, text="")
    canvas.itemconfig(card_word, text="")

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")


window.after(3000, flip_card)

window.mainloop()
