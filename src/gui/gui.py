from tkinter import *

window = Tk()

input_user = StringVar()
input_field = Entry(window, text=input_user)
input_field.pack(side=BOTTOM, fill=X)

def Enter_pressed(event):
    input_get = input_field.get()
    print(input_get)
    label = Label(window, text=input_get)
    input_user.set('')
    label.pack()
    return "break"

frame = Frame(window, width=300, height=300)
input_field.bind("<Return>", Enter_pressed)
frame.pack()

window.mainloop()
