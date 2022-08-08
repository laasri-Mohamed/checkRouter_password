import random
import webbrowser
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import back
import csv
from ttkbootstrap import *
from datetime import datetime


 
 
class window:
    # these are lists of initialized characters
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
     
     
    lc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
          'm', 'n', 'o', 'p', 'q',
          'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
     
    uc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
          'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
          'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
     
    sym = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|',
           '~', '>', '*', '<']
     
    def __init__(self, root, geo, title) -> None:
        self.root = root
        self.root.title(title)
        self.root.geometry(geo)
        self.root.resizable(width=False, height=False)
 
        Label(self.root, text='Your Password').grid(row=1, column=0, padx=10, pady=10)
        Label(self.root, text='Date').grid(row=2, column=0, padx=10, pady=10)
        Label(self.root, text='Url').grid(row=0, column=0, padx=10, pady=10)
        self.pa = StringVar()
        self.date = StringVar()
        self.url = StringVar()
        ttk.Entry(self.root, width=30, textvariable=self.pa
                 ).grid(row=1, column=1, padx=4, pady=4)
        ttk.Entry(self.root, width=30, textvariable=self.date
                 ).grid(row=2, column=1, padx=4, pady=4)
        ttk.Entry(self.root, width=30, textvariable=self.url
                 ).grid(row=0, column=1, padx=4, pady=4)
        self.length = StringVar()
 
        e = ttk.Combobox(self.root, values=['4', '8', '12', '16', '20', '24','28','32'],
                         textvariable=self.length)
        e.grid(row=0, column=2)
        e['state'] = 'readonly'
        self.length.set('Set password length')
 
        ttk.Button(self.root, text='Generate', padding=5,
                   style='success.Outline.TButton', width=20,
                   command=self.generate).grid(row=1, column=2)
         
        ttk.Button(self.root, text='Save to Database', style='success.TButton',
                   width=20, padding=5, command=self.save).grid(row=3, column=2)
         
        ttk.Button(self.root, text='Delete', width=20, style='danger.TButton',
                   padding=5, command=self.erase).grid(row=2, column=2)

        ttk.Button(self.root, text='Dernier', width=20, style='success.TButton',
                   padding=5, command=self.dernier).grid(row=3, column=0)
        
        ttk.Button(self.root, text='Search', width=20, style='danger.TButton',
                   padding=5, command=self.search).grid(row=5, column=2)
         
        
         
        ttk.Button(self.root, text='Update', width=20, padding=5,
                   command=self.update).grid(row=3, column=1)
 
        # ========self.tree view=============
        self.tree = ttk.Treeview(self.root, height=5)
        self.tree['columns'] = ('date', 'pas')
        self.tree.column('#0', width=0, stretch=NO)
        self.tree.column('date', width=160, anchor=W)
        self.tree.column('pas', width=180, anchor=W)
        self.tree.heading('#0', text='')
        self.tree.heading('date', text='date name')
        self.tree.heading('pas', text='Password')
 
        self.tree.grid(row=4, column=0, columnspan=3, pady=10)
        self.tree.bind("<ButtonRelease-1>", self.catch)
        #  cette commande appellera la fonction catch
 
        # ceci est le menu contextuel du clic droit
        self.menu = Menu(self.root, tearoff=False)
        self.menu.add_command(label='Refresh', command=self.refresh)
        self.menu.add_command(label='Insert', command=self.save)
        self.menu.add_command(label='Update', command=self.update)
        self.menu.add_separator()
        self.menu.add_command(label='Show All', command=self.view)
        self.menu.add_command(label='Clear Fields', command=self.clear)
        self.menu.add_command(label='Clear Table', command=self.table)
        self.menu.add_command(label='Export', command=self.export)
        self.menu.add_separator()
        self.menu.add_command(label='Delete', command=self.erase)
        self.menu.add_command(label='Help', command=self.help)
        self.menu.add_separator()
        self.menu.add_command(label='Exit', command=self.root.quit)
        # ceci lie le bouton 3 de la souris avec
        self.root.bind("<Button-3>", self.poppin)
        # fonction poppin
 
    def help(self):
        # cette fonction ouvrira le fichier help.txt dans
        #  bloc-notes lorsqu'il est appelé
        webbrowser.open('help.txt')
 
    def refresh(self):
        # cette fonction rafraîchit essentiellement la table
        # ou arborescence
        self.table()
        self.view()
 
    def table(self):
        # cette fonction effacera toutes les valeurs
        # affiché dans le tableau
        for r in self.tree.get_children():
            self.tree.delete(r)
 
    def clear(self):
        # cette fonction effacera toutes les entrées
        # des champs
        self.pa.set('')
        self.date.set('')
 
    def poppin(self, e):
        # il déclenche le menu contextuel du clic droit
        self.menu.tk_popup(e.x_root, e.y_root)
 
    def catch(self, event):
        # cette fonction prendra toutes les données sélectionnées
        # e la table/arborescence et remplira le
        # champs de saisie respectifs
        self.pa.set('')
        self.date.set('')
        selected = self.tree.focus()
        value = self.tree.item(selected, 'value')
        self.date.set(value[0])
        self.pa.set(value[1])
 
    def update(self):
        # cette fonction mettra à jour la base de données avec de nouveaux
        # valeurs données par l'utilisateur
        selected = self.tree.focus()
        value = self.tree.item(selected, 'value')
        back.edit(self.date.get(), self.pa.get())
        self.refresh()
 
    def view(self):
        # cela affichera toutes les données de la base de données
        # ceci est similaire à "SELECT * FROM TABLE" sql
    
        if back.check() is False:
            messagebox.showerror('Attention Amigo!', 'Database is EMPTY!')
        else:
            for row in back.show():
                self.tree.insert(parent='', text='', index='end',
                                 values=(row[0], row[1]))
 
    def erase(self):
        # cela supprimera ou supprimera le tuple sélectionné ou
        # ligne de la base de données
        selected = self.tree.focus()
        value = self.tree.item(selected, 'value')
        back.Del(value[1])
        self.refresh()
 
    def save(self):
        # cette fonction insèrera toutes les données dans le
        # base de données
        back.enter(self.date.get(), self.pa.get())
        self.tree.insert(parent='', index='end', text='',
                         values=(self.date.get(), self.pa.get()))
 
    def generate(self):
        # cette fonction produira une chaîne aléatoire qui
        # sera utilisée comme mot de passe
        if self.length.get() == 'Set password length':
            messagebox.showerror('Attention!', "You forgot to SELECT")
        else:
            a = ''
            for x in range(int(int(self.length.get())/4)):
                a0 = random.choice(self.uc)
                a1 = random.choice(self.lc)
                a2 = random.choice(self.sym)
                a3 = random.choice(self.digits)
                a = a0+a1+a2+a3+a
                self.pa.set(a)
            b = datetime.today().strftime('%Y-%m-%d  %H:%M:%S')  
            self.date.set(b)
            mot_de_passe =a
            print("le nouveau mot de passe est: "+mot_de_passe)
    
    def dernier(self):
        back.last()   
    def search(self):
        back.URL(self.url.get()) 

    def export(self):
        # cette fonction sauvegardera toutes les données du
        # base de données au format csv qui peut être ouvert
        # dans excel

        pop = Toplevel(self.root)
        pop.geometry('300x100')
        self.v = StringVar()
        Label(pop, text='Save File Name as').pack()
        ttk.Entry(pop, textvariable=self.v).pack()
        ttk.Button(pop, text='Save', width=18,
                   command=lambda: exp(self.v.get())).pack(pady=5)
 
        def exp(x):
            with open(x + '.csv', 'w', newline='') as f:
                chompa = csv.writer(f, dialect='excel')
                for r in back.show():
                    chompa.writerow(r)
            messagebox.showinfo("File Saved", "Saved as " + x + ".csv")
 
 
if __name__ == '__main__':
    win = Style(theme='darkly').master
    name = 'Password Generator'
    dimension = '565x320'
 
    app = window(win, dimension, name)
    win.mainloop()