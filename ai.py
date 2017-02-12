from tkinter import *




master = Tk()
master.title("John")
master.iconbitmap('favicon.ico')

L1 = Label(master, text="Hello my name is John, I am your personal servant. How may I help you?...")
L1.pack( side = LEFT)
E1 = Entry(master, bd =5)
E1.pack(side = RIGHT)

mainloop()
