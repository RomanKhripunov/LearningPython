import sys
from tkinter import *

window = Tk()

window.title("Welcome to LikeGeeks app")
window.geometry('600x300')

b1 = Button(window, text='One')
b2 = Button(window, text='Two')

b1.grid(row=0, column=0)
b2.grid(row=1, column=1)

# label_b2 = Label(window, text='Button N2')
# label_b2.grid(row=1, column=0)

window.mainloop()