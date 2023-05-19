from tkinter import *
from tkinter import colorchooser

root = Tk()

def choose_color():
    color = colorchooser.askcolor()
    print(color)

Button(root, text="Escolher cor", command=choose_color).pack()

root.mainloop()