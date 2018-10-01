# -*- coding: utf-8 -*-

from Tkinter import *
from ttk import *

prgprincipal = Tk() #version du programme : alpha build 0.0.2

version = 2

prgprincipal.geometry ("300x700+450+500")
prgprincipal.title ("Amélia alpha build")

def aboutwindow():
    about = Tk()
    about.geometry ("300x90+350+400")
    about.title ("A propos d'Amélia")

    
    label = Label(about, text="Amélia est un logiciel libre. Codé en Python 2.7")
    label.pack()
    
    label = Label(about, text="par Mael Le Boulicaut et Evan Diberder")           
    label.pack()

    label = Label(about, text="Version Alpha 0.0.2, License GPL V3")           
    label.pack()

    
    canvas = Canvas(aboutwindow,width=60, height=25)
    canvas.create_image(1000, 1000, anchor=NW, image=visageAmelia)
    canvas.pack()

def Enter_pressed(event):
    input_get = input_field.get()
    if input_get == ("salut"):
        label = Label(prgprincipal, text="hello")
    elif input_get == ("ca va"):
        label = Label(prgprincipal, text="Bien sur et vous ?")
    elif input_get == ("comment ca va"):
        label = Label(prgprincipal, text=" Ca va bien et vous ?"
    elif input_get == ("Je suis nul"):
        label = Label(prgprincipal, text="Bien sur "
    elif input_get == ("Tu m aime"):
        label = Label(prgprincipal, text="Bah non quelle question !"
    elif input_get == ("connard"):
        label = Label(prgprincipal, text="La PS4 dans crane à ta mère"
    elif input_get == ("je comprends rien au math"):
        label = Label(prgprincipal, text="NANI"

    else:
        label = Label(prgprincipal, text="Je n'ai pas compris")
    input_user.set('')
    label.pack()
    return "break"

menubar = Menu(prgprincipal)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Proposer un tuto pour un logiciel")
menu1.add_separator()
menu1.add_command(label="Quitter", command=prgprincipal.quit)
menubar.add_cascade(label="Amélia", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Preferences")
menu2.add_command(label="Copier")
menu2.add_command(label="Coller")
menubar.add_cascade(label="Options", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos de Amelia", command=aboutwindow)
menubar.add_cascade(label="Aide", menu=menu3)

visageAmelia = PhotoImage(file="amelia.png")

prgprincipal.config(menu=menubar)

canvas = Canvas(prgprincipal,width=180, height=300)
canvas.create_image(0, 0, anchor=NW, image=visageAmelia)
canvas.pack()

input_user = StringVar()
input_field = Entry(prgprincipal, text=input_user)
input_field.pack(side=BOTTOM, fill=X)

input_field.bind("<Return>", Enter_pressed)

prgprincipal.style = Style()
#Voici les différents styles : 'clam', 'alt', 'default', 'classic'
prgprincipal.style.theme_use("alt")

prgprincipal.mainloop()


