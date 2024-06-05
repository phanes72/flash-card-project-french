from tkinter import *
import pandas as pd
import random

data = pd.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

to_learn_card = {}
current_card = random.choice(to_learn)


# https://stackoverflow.com/questions/75966783/pycharm-error-expected-type-class-name-got-str-instead
def update_learn_list():
    csv_file_path = "data/words_to_learn.csv"
    # data.to_csv(csv_file_path, index=False)

    to_learn.remove(current_card)
    df = pd.DataFrame(to_learn)
    df.to_csv(csv_file_path, index=False)

    print(current_card["French"] + " " + current_card["English"])


def next_card():
    canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="white")
    canvas.itemconfig(card_word, text=current_card["French"], fill="white")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.config(bg="white", highlightthickness=0)
    canvas.itemconfig(card_title, text="")

    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")

    update_learn_list()


canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_title = canvas.create_text(400, 150, text="English", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text=current_card["English"], font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

flip_timer = window.after(3000, flip_card)

window.mainloop()
