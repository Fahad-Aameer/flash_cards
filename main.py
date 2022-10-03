from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    language_data_frame = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    language_data_frame = pandas.read_csv("french_words.csv")

dict_lang = language_data_frame.to_dict(orient="records")
the_word = []

def next_card():
    global the_word
    canvas.itemconfig(canvas_image, image=front_card)
    the_word = random.choice(dict_lang)
    res = list(the_word.keys())[0]
    res1 = list(the_word.keys())[1]
    canvas.itemconfig(lang, text=str(res), fill="black")
    canvas.itemconfig(word, text=the_word['French'], fill="black")
    window.after(3000, answer_card, the_word['English'], res1)

def is_known():
    dict_lang.remove(the_word)
    data = pandas.DataFrame(dict_lang)
    data.to_csv("words_to_learn.csv", index=False)

    next_card()


def answer_card(a, b):
    canvas.itemconfig(canvas_image, image=back_card)
    canvas.itemconfig(lang, text=b, fill="white")
    canvas.itemconfig(word, text=a, fill="white")


window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="card_front.png")
canvas_image = canvas.create_image(400, 263, image=front_card)
back_card = PhotoImage(file="card_back.png")
lang = canvas.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

rightImg = PhotoImage(file="right.png")
button_tick = Button(image=rightImg, highlightthickness=0, command=is_known)
button_tick.grid(column=1, row=1)

wrongImg = PhotoImage(file="wrong.png")
button_cross = Button(image=wrongImg, highlightthickness=0, command=next_card)
button_cross.grid(column=0, row=1)

next_card()

window.mainloop()
