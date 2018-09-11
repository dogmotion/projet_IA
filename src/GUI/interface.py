# -*- coding: utf-8 -*-

from Tkinter import *
from ttk import *

prgprincipal = Tk() #version du programme : alpha build 0.0.2

prgprincipal.geometry ("700x500+450+500")
prgprincipal.title ("Amélia alpha build 0.0.2")

def aboutwindow():
    about = Tk()
    about.geometry ("700x100+350+400")
    about.title ("A propos d'Amélia")

    
    label = Label(about, text="Amélia est un programme libre creer en Python")
    label.pack()
    
    label = Label(about, text="par Mael Le Boulicaut et Evan Diberder")           
    label.pack()

    label = Label(about, text="version alpha 0.0.2")           
    label.pack()

    
    canvas = Canvas(aboutwindow,width=48, height=48)
    canvas.create_image(1000, 1000, anchor=NW, image=visageAmelia)
    canvas.pack()

def lienInAmelia():

     import gtk  
     import webkit  
     import gobject
     
     gobject.threads_init()  
     window = gtk.Window()
     window.set_default_size(1100, 680)
     window.connect("destroy", lambda a: gtk.main_quit()) 
     browser = webkit.WebView()  
     browser.open("http://alfred-ia.org/essaye-moi/")  
     window.add(browser)  
     window.show_all()  
     gtk.main()
          
menubar = Menu(prgprincipal)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="En attendant : Testez Alfred", command=lienInAmelia)
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

prgprincipal.config(menu=menubar)



label = Label(prgprincipal, text="Coucou !")
label.pack()

label = Label(prgprincipal, text="Dit moi tout")
label.pack()


visageAmelia = PhotoImage(file="amelia.png")


canvas = Canvas(prgprincipal,width=500, height=500)
canvas.create_image(0, 0, anchor=NW, image=visageAmelia)
canvas.pack()


prgprincipal.style = Style()
#Voici les diferents styles : 'clam', 'alt', 'default', 'classic'
prgprincipal.style.theme_use("clam")


prgprincipal.mainloop()


