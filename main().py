from listestudent import *


dbconnect=dbclass()

#window
wind=Tk()


#BACKGROUND
logo=Image.open("backgroun1.png")
im=logo.resize((150,477))
render = ImageTk.PhotoImage(im)

#CANVAS
canvas=Canvas(wind,width=300,height=160)
canvas.create_image(0,0,anchor=NW,image=render)
canvas.pack(fill=BOTH,expand=1)

#style
style=ttk.Style()
style.configure('TLabel',foreground='#E51919')
style.configure('TButton',foreground='#E51919')
style.configure('TRadiobutton',foreground='#E51919')

#title
wind.title("Application de gestion des notes")

#Nome & Prénom
ttk.Label(canvas,text='Nom & Prénom :*').grid(row=0,column=0,padx=10,pady=15)
entername=ttk.Entry(canvas,width=35,font=('fixedsys',15))
entername.grid(row=0,column=1,columnspan=3,padx=10,pady=15)

#Note
ttk.Label(canvas,text='Note   : *').grid(row=2,column=1,padx=10,pady=15)
enternote=ttk.Entry(canvas,width=5,font=('system',10))
enternote.grid(row=2,column=2,padx=10,pady=15)

#Redoblant
ttk.Label(canvas,text='Redoublant   : *').grid(row=3,column=1,padx=10,pady=15)
var=StringVar()
ttk.Radiobutton(canvas,text='Oui',variable=var,value="Oui").grid(row=3,column=2)
ttk.Radiobutton(canvas,text='Non',variable=var,value="Non").grid(row=3,column=3)

#Appréciations
ttk.Label(canvas,text='Appréciations  :').grid(row=4,column=1,padx=10,pady=15)
txt=Text(canvas,width=20,height=15,font=('ms serif',10))
txt.grid(row=4,column=2,columnspan=2,padx=15,pady=5,sticky='snew')

#Button LISTE DES NOTES
liste=ttk.Button(canvas,text='LISTE DES NOTES')
liste.grid(row=6,column=2,padx=10,pady=10)

#Button AJOUTER
ajouter=ttk.Button(canvas,text='AJOUTER')
ajouter.grid(row=6,column=3,padx=10,pady=10)

#Command : Button AJOUTER
def fajouter():

    if not (not var.get() or not entername.get() ):
        try :  #exception pour que le type de note se soit un nombre

                msg=dbconnect.ajouter(entername.get(),float(enternote.get()),var.get(),txt.get("1.0",END))  #Method qui ajout un elem -->DB
                messagebox.showinfo(title='Nouvel Ajout',message=msg)

        except ValueError:
                messagebox.showerror(title='ERROE', message='assurez-vous de saisir une Note sous forme _par exemple_ (11.00) ')
    else :
        messagebox.showerror(title='ERROR', message='Veuillez remplir tous les champs marqués d`un astérisque(*)')
ajouter.config(command=fajouter)

#Command : Button liste
def lister():
    liste=listestudents()

liste.config(command=lister)



wind.mainloop()