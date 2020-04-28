from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from database import *
from PIL import Image,ImageTk
db=dbclass()
class modifier:
    def __init__(self,id):
        root = Tk()
        root.title('changer la note')
        root.geometry('300x150')

        #Label : NOUVELLE NOTE
        ttk.Label(root, text='Nouvelle Note  :').grid(row=0, column=1)
        note=ttk.Entry(root, width=5, font=('system', 10))
        note.grid(row=0, column=2)

        #Button : MODIFIER
        but = ttk.Button(root, text="MODIFIR")
        but.grid(row=1, column=2)

        def changer():
            try :
                msg=db.modifier(id,float(note.get()))
                messagebox.showinfo(message=msg)
                root.destroy()
            except ValueError:
                messagebox.showerror(title='ERROE', message='assurez-vous de saisir une Note sous forme _par exemple_ (11.00) ')
        but.config(command=changer)