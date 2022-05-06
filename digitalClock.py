from cProfile import label
from curses import window
from datetime import datetime
from time import time
from tkinter import Tk, Label

window = Tk()
window.title("Digital Clock")
window.geometry("600x300")
window.configure(bg="red")

label = Label(window, font=("Ariel Black",78,"bold"), bg="red", fg="white")
label.pack(pady=100) 

def clock():
    time  = datetime.now().strftime("%H:%M:%S")
    label.configure(text=time)
    label.after(500,clock)

clock()
window.mainloop()