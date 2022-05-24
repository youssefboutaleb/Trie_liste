from tkinter import *
from tkinter.messagebox import *

""" MES FONCTIONS """
liste_trie = []
liste_non_trie = []


def enregistrement(event):
    # la fonction qui ajoute un nouvel element
    global liste_trie, liste_non_trie
    try:
        int(element_ajoute.get())
        listebox_non_triee.insert(END, element_ajoute.get())  # l'element s'affiche dans le box non trié
        liste_trie.append(int(element_ajoute.get()))  # les elements s'affiche dans le box trié
        element_ajoute.set('')
    except (ValueError):
        showinfo("Attention", "Il faut entrer un entier")
        element_ajoute.set('')


def supprission(*args):
    # la fonction qui supprime des elements de la liste
    global liste_trie, liste_non_trie
    index = listebox_non_triee.curselection()[0]  # l'indice de l'element qu'on veut supprimer
    listebox_non_triee.delete(int(index))  # l'elemnet n'est plus affiché dans la listebox
    del liste_non_trie[index]  # l'element se supprime de l la liste non triée
    liste_trie = liste_non_trie[
                 :]  # on prend une copie de la liste non triée pour faire la trie encore une fois sans l'element supprimé


# tri par insertion
def tri_insertion_croissante(tab):
    for i in range(1, len(tab)):
        v = tab[i]
        j = i
        while (tab[j - 1] > v) and (j > 0):
            tab[j] = tab[j - 1]
            j -= 1
        tab[j] = v
    return (tab)


def tri_insertion_decroissante(tab):
    for i in range(1, len(tab)):
        v = tab[i]
        j = i
        while (tab[j - 1] < v) and (j > 0):
            tab[j] = tab[j - 1]
            j -= 1
        tab[j] = v
    return (tab)


# la fonction qui s'execute lorsqu'on presse le bouton trié
def tri(*args):
    global liste_trie, liste_non_trie
    # on trie la liste triée selon le mode selectionnée
    if (mode_choisi.get() == "tri croissant"):
        liste_trie = tri_insertion_croissante(liste_trie)
    else:
        liste_trie = tri_insertion_decroissante(liste_trie)
        listebox_triee.delete(0, END)  # on supprime tout ce qui est affichée dans la listebox triée
    for i in range(0, len(liste_trie)):
        listebox_triee.insert(END, liste_trie[i])  # on remplie la listebox triée avec les elements de la liste triée


"""" L'INTERFACE """
fenetre = Tk()
fenetre.title("Trie des tableaux")

""" la demande d'un entier """
texte_donner_element = Label(fenetre, text="Donner un element     ")  # on affiche la phrase Donner un element
texte_donner_element.grid(row=1, column=0)  # la position de la phrase

element_ajoute = StringVar()  # l'element ajoute
box_donner_element = Entry(fenetre, textvariable=element_ajoute, width=15)  # le box ou on va ajouter l'element
box_donner_element.grid(row=1, column=1)  # la position du box
box_donner_element.bind('<Return>', enregistrement)  # on cliquant la touche entree du clavier on ajoute un element

""" l'affichage des elements"""
listebox_non_triee = Listbox(fenetre, heigh=7, width=15)  # la listebox ou on va afficher les elements non tries
listebox_non_triee.grid(column=1, row=2)  # la position du listebox
scro1l1 = Scrollbar(fenetre, orient=VERTICAL, command=listebox_non_triee.yview)  # on cree un vertical scrollbar
scro1l1.grid(column=2, row=2, sticky=(N, S))  # la position du scrollbar
listebox_non_triee['yscrollcommand'] = scro1l1.set
listebox_non_triee.bind('<Double-1>', supprission)  # si on clique a un element du liste box il se supprime

""" selection du tri """
mode_choisi = StringVar()  # le mode de tri
mode_tri = Label(fenetre, text="choisir un mode de tri:      ")  # on affiche la phrase choisir un mode de tri:
mode_tri.grid(row=3, column=0)  # la position de la phrase

tri_croissant = Radiobutton(fenetre, text="tri croissant", variable=mode_choisi,
                            value='tri croissant')  # le bouton pour choisir le tri croissant
tri_decroissant = Radiobutton(fenetre, text="tri decroissant", variable=mode_choisi,
                              value='tri decroissant')  # le bouton pour choisir le tri decroissant
tri_croissant.grid(column=1, row=3, sticky=W, padx=20)  # la position du bouton du tri croissant
tri_decroissant.grid(column=1, row=4, sticky=W, padx=20)  # la position du bouton du tri croissant
mode_choisi.set("tri croissant")  # on met le tri croissant selectionne par defaut

""" le bouton de tri """
trierbtn = Button(fenetre, text='  trier  ', command=tri, default='active')  # le bouton qui execute la tri
trierbtn.grid(column=1, row=6, sticky=E, padx=10, pady=10)  # la position du bouton

""" l'affichage des elements tries """
listebox_triee = Listbox(fenetre, heigh=7, width=15)  # la listebox ou on va afficher les elements tries
listebox_triee.grid(column=1, row=7)  # la position du listebox
scroll2 = Scrollbar(fenetre, orient=VERTICAL, command=listebox_triee.yview)  # on cree un vertical scrollbar
scroll2.grid(column=2, row=7, sticky=(N, S))  # la position du scrollbar
listebox_triee['yscrollcommand'] = scroll2.set

fenetre.mainloop()

