import tkinter
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
# window.config(padx=20, pady=20, )
window.geometry("900x700")


canvas = Canvas(window, width=800, height=626)
card_front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 300, image=card_front_image)
# canvas.grid(row=0, column=0)
canvas.pack()

# right_canvas = Canvas(window, width=400, height=300)
# right_image = PhotoImage(file="images/right.png")
# right_canvas.create_image(20, 20, anchor='sw', image=right_image)
# # right_canvas.grid(row=1, column=0)
#
# wrong_canvas = Canvas(window, width=400, height=300)
# wrong_image = PhotoImage(file="images/wrong.png")
# canvas.create_image(20,20, anchor='se', image=wrong_image)
# canvas.grid(row=1, column=1)

window.mainloop()
