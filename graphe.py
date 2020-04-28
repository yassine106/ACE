import tkinter as tk
from tkinter import ttk
from database import *
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



db=dbclass()
class graphe():
    def __init__(self):
        self.db=dbclass()
        liste=self.db.liste()

        p1=[] #liste pour les noms des etudiants
        p2=[] #liste pour les notes des etudiants


        f=0 #pour le nombre des etudiants qui n'ont pas réussi
        s=0 #pour le nombre des etudiants qu'ont réussi

        for i in liste:
            p1.append(i['Nom'])
            p2.append(float(i['Note']))

            if float(i['Note']) < 11 :
                f+=1
            else:
                s+=1


        data1 = {'ETUDIANTS': p1, 'NOTE': p2 }
        df1 = DataFrame(data1, columns=['ETUDIANTS', 'NOTE'])

        data2 = {'TYP': ['ont réussi','n’ont pas réussi'],'SNOTE':[s,f] }
        df2 = DataFrame(data2, columns=['TYP', 'SNOTE'])


        #Fenêtre : Pour les graphes
        root = tk.Tk()
        root.title('Graphe')

        #GRAPHE 1 :
        figure1 = plt.Figure(figsize=(10,10), dpi=80)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, root)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df1 = df1[['ETUDIANTS', 'NOTE']].groupby('ETUDIANTS').sum()
        df1.plot(kind='bar', legend=True, ax=ax1)
        ax1.set_title('NOTES DES ETUDIANTS')

        #GRAPHE 2
        figure2 = plt.Figure(figsize=(10,5), dpi=80)
        ax2 = figure2.add_subplot(111)
        bar2 = FigureCanvasTkAgg(figure2, root)
        bar2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df2 = df2[['TYP', 'SNOTE']].groupby('TYP').sum()
        df2.plot(kind='pie',subplots=True, ax=ax2)
        ax2.set_title('TAUX DE REUSSITE')



        root.mainloop()


