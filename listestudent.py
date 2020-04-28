from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from database import *
from modifier import *
from graphe import *
x=0
class listestudents():
    def __init__(self):
        self.window=Tk()
        self.db=dbclass()
        self.window.title('Tableau des étudiants')

        #CANVAS
        canvas = Canvas(self.window, width=700, height=560)
        canvas.pack()
        canvas2 = Canvas(self.window, width=1, height=60)
        canvas2.pack()

        #TREEVIEW
        tv=ttk.Treeview(canvas)
        tv.grid(row=0,column=0,sticky='snew')


        butg=ttk.Button(canvas,text='AFFICHER LES GRAPHES')  #Button : AFFICHER LES GRAPHES
        butg.grid(row=1,column=0,columnspan=2,sticky='snew')

        tv.heading('#0',text='ID')
        tv.configure(column=('#Nom','#Note','#Redoublant','#Comment',))
        tv.column('#Nom', anchor='center')
        tv.column('#Note',anchor='center')
        tv.column('#Redoublant', anchor='center')
        tv.heading('#Nom', text='Nom')
        tv.heading('#Note', text='Note')
        tv.heading('#Redoublant', text='Redoublant')
        tv.heading('#Comment', text='Comment')
        liste=self.db.liste()

        #INSERER LES DONNEES BD-->FENETRE
        for i in liste:
            tv.insert('','end','{}'.format(i['id']),text=i['id'])
            tv.set('{}'.format(i['ID']),'#Nom','{}'.format(i['Nom']))
            tv.set('{}'.format(i['ID']), '#Note', '{}'.format(i['Note']))
            tv.set('{}'.format(i['ID']), '#Redoublant', '{}'.format(i['Redoublant']))
            tv.set('{}'.format(i['ID']), '#Comment', '{}'.format(i['Comment']))

        #QUITTER LA FENETRE D
        def quite():
            global x
            x=0
            self.window.destroy()
        #Button :quitter
        quit = ttk.Button(canvas2, text='QUITER')
        quit.pack()
        quit.config(command=quite)

        #SUPPRIMER OU MODIFIER UN ELEMENT Selectionné
        label=ttk.Label(self.window,text='Selectionner un etudient pour le supprimer ou modifier')
        label.pack()
        sup = ttk.Button(self.window, text='SUPPRIMER')
        mod = ttk.Button(self.window, text='MODIFIER')
        def selection(event):
            label.pack_forget()
            global x
            global y
            y=tv.selection()
            if x==0 :
                sup.pack()
                mod.pack()
                ttk.Label(self.window, text='Redemarer cette fenetre pour voir les modifications').pack()
                x=1
        tv.bind('<<TreeviewSelect>>',selection)

        #configurer button supp
        def supprimer():
            msg=self.db.supprimer(y)
            messagebox.showinfo(message=msg)
        sup.config(command=supprimer)

        #configurer button supp
        def modif():
            new=modifier(y)
        mod.config(command=modif)

        # configurer button AFFICHER LES GRAPHES
        def plot():
            ploot=graphe()
        butg.config(command=plot)


        self.window.mainloop()

