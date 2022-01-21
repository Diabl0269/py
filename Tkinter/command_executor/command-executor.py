from tkinter import Tk, Label, Entry, Button, Text
from functions import *


def handle_click():
    output = execute(ent.get())
    txt.insert("0.0", output)


window = Tk()
window.title("Command executor")
window.geometry("400x400")
window.resizable(False, False)

lbl = Label(window, text="Command")
lbl.place(x=10, y=15)

ent = Entry(window)
ent.place(x=85, y=15)

btn = Button(window, width=8, height=1, command=handle_click, text="Execute")
btn.place(x=280, y=12)

txt = Text(window, width=53)
txt.place(x=10, y=50)

window.mainloop()
