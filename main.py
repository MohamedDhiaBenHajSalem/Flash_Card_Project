BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"


from tkinter import Tk,Canvas,PhotoImage,Button
import pandas
import random
import time

try :
    file=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    file=pandas.read_csv("data/french_words.csv")

dict_file=file.to_dict(orient="records")


current_card={}
words_to_learn={}
def next_word():
    global current_card,flip_timer

    Window.after_cancel(flip_timer)

    current_card=random.choice(dict_file)

    canvas.itemconfig(main_Image,image=card_front)

    canvas.itemconfig(card_Titel,text="French",fill="black")
    canvas.itemconfig(card_World,text=current_card["French"],fill="black")
    flip_timer=Window.after(3000, flip_card)






def flip_card():
    canvas.itemconfig(main_Image, image=card_back)
    canvas.itemconfig(card_Titel, text="English", fill="white")
    canvas.itemconfig(card_World, text=current_card["English"], fill="white")


def add_word():
   global words_to_learn

   dict_file.remove(current_card)
   data=pandas.DataFrame(dict_file)
   data.to_csv("data/words_to_learn.csv",index=False)
   next_word()




Window=Tk()
Window.title("Flashy")
Window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)
flip_timer=Window.after(3000,flip_card)

canvas=Canvas(width=800,height=526)
X_Image=PhotoImage(file="images/wrong.png")
V_Image=PhotoImage(file="images/right.png")
card_front=PhotoImage(file='images/card_front.png')
card_back=PhotoImage(file="images/card_back.png")

main_Image=canvas.create_image(400,263,image=card_front)
card_Titel=canvas.create_text(400,150,text="",fill="black",font=("Ariel",40,"italic"))
card_World=canvas.create_text(400,263,text="",fill="black",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)

canvas.grid(row=0,column=0,columnspan=2)


button_right=Button(image=V_Image,highlightthickness=0,command=add_word)
button_right.grid(row=1,column=0)
button_wrong=Button(image=X_Image,highlightthickness=0,command=next_word)
button_wrong.grid(row=1,column=1)

next_word()

Window.mainloop()