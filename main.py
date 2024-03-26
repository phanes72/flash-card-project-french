import tkinter
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
# window.config(padx=20)
window.geometry("1000x800")


canvas = Canvas(window, width=800, height=800)
card_front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 300, image=card_front_image)
canvas.grid(row=0, column=1)
# canvas.pack()

right_canvas = Canvas(window, width=100, height=100)
right_image = PhotoImage(file="images/right.png")
right_canvas.create_image(50, 600, image=right_image)
# right_canvas.pack()
right_canvas.grid(row=1, column=0)

wrong_canvas = Canvas(window, width=400, height=650)
wrong_image = PhotoImage(file="images/wrong.png")
canvas.create_image(600, 620, image=wrong_image)
canvas.grid(row=1, column=2)

window.mainloop()
