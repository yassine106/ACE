import sqlite3

from tkinter import messagebox
class dbclass:
    def __init__(self):
        #creer database
        self.db=sqlite3.connect('gestion_des_notes.db')
        #possibilité de modifier sur la database
        self.db.row_factory=sqlite3.Row
        #create table student
        self.db.execute("create table if not exists student(id INTEGER primary key autoincrement,Nom TEXT,Note INTEGER ,Redoublant TEXT,Comment TEXT)")
        #enregister ces info sur database
        self.db.commit()

    #Method : AJOUTER
    def ajouter(self,nom,note,redoublant,comment):
        self.db.execute("insert into student(Nom,Note,Redoublant,Comment) values (?,?,?,?)",(nom,note,redoublant,comment))
        self.db.commit()
        return "Ajout avec succés"

    #Method : LISTE DES NOTES
    def liste(self):
        liste=self.db.execute("select * from student")
        return liste

    #Methode : SUPPRIMER
    def supprimer(self,id):
        print(id)
        self.db.execute("delete from student where id = (?)",(id))
        self.db.commit()
        return "supprission avec succés"

    #Method : MODIFIER
    def modifier(self,id,note):
        self.db.execute("update student set Note=(?) where id =(?)",(note,id[0]))
        self.db.commit()
        return "Modification  avec succés"