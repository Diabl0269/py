from tkinter import Tk, Button, Entry, END
from helpers import *

operators = ["+", "-", "*", "/", "="]

# Constants
XStep = 125
YStep = 40
YStart = 40
XStart = 10

# Initialize
y = YStart
calculator = Calculator()
window = Tk()
window.title("Calculator")
window.geometry("500x220")

ent = Entry(window, width=52)
ent.place(x=12, y=10)


# UI functions
def handle_input(inp):
    def add_entry(entry=inp):
        ent.insert(END, entry)

    return add_entry


def handle_action(action):
    def switch_actions(act=action):
        if act == '+':
            calculator.operator = "+"
            set_num()
            handle_delete()
        if act == '-':
            calculator.operator = "-"
            set_num()
            handle_delete()
        if act == '/':
            calculator.operator = "/"
            set_num()
            handle_delete()
        if act == '*':
            calculator.operator = "*"
            set_num()
            handle_delete()
        if act == '=':
            set_num()
            handle_delete()
            calculator()
            ent.insert(0, calculator.result)
        if act == 'clear':
            handle_delete()
            calculator.clear()

    return switch_actions


def handle_delete():
    ent.delete(0, END)


def set_num():
    if not calculator.current_input:
        calculator.num1 = ent.get()
    else:
        calculator.num2 = ent.get()
    calculator.current_input = not calculator.current_input


# Buttons data
elements = [[{"text": "1", "handle_click": handle_input("1")}, {"text": "2", "handle_click": handle_input("2")},
             {"text": "3", "handle_click": handle_input("3")}, {"text": "+", "handle_click": handle_action("+")}],
            [{"text": "4", "handle_click": handle_input("4")}, {"text": "5", "handle_click": handle_input("5")},
             {"text": "6", "handle_click": handle_input("6")}, {"text": "-", "handle_click": handle_action("-")}],
            [{"text": "7", "handle_click": handle_input("7")}, {"text": "8", "handle_click": handle_input("8")},
             {"text": "9", "handle_click": handle_input("9")}, {"text": "*", "handle_click": handle_action("*")},
             ],
            [{"text": "Clear", "handle_click": handle_action("clear")},
             {"text": "0", "handle_click": handle_input("0")},
             {"text": "=", "handle_click": handle_action("=")}, {"text": "/", "handle_click": handle_action("/")},
             ]
            ]

# Create buttons
for i, elements_row in enumerate(elements):
    x = XStart
    if i != 0:
        y += YStep
    for element in elements_row:
        btn = Button(window, width=8, height=2, text=element.get("text"), command=element.get("handle_click"))
        btn.place(x=x, y=y)
        x += XStep

window.mainloop()
