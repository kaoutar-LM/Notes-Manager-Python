import tkinter as tk
from tkinter import messagebox

# Liste des notes (elle sera partagée entre les fonctions)
notes = []

# Fonctions de gestion des notes (elles restent inchangées)
def ajouter_note():
    note = entry_note.get()  # On récupère la note depuis le champ de texte
    if note:
        notes.append(note)  # Ajout de la note à la liste
        listbox_notes.insert(tk.END, note)  # Ajout de la note à la liste dans l'interface
        entry_note.delete(0, tk.END)  # On vide le champ de texte
    else:
        messagebox.showwarning("Entrée vide", "Veuillez entrer une note.")

def supprimer_note():
    try:
        selected_index = listbox_notes.curselection()[0]  # Récupérer l'index de la note sélectionnée
        removed_note = notes.pop(selected_index)  # On retire la note de la liste des notes
        listbox_notes.delete(selected_index)  # On retire la note de la liste affichée dans l'interface
        messagebox.showinfo("Note supprimée", f"Note '{removed_note}' supprimée.")
    except IndexError:
        messagebox.showwarning("Sélection invalide", "Veuillez sélectionner une note à supprimer.")

def sauvegarder_notes():
    with open("notes.txt", "w") as file:
        for note in notes:
            file.write(note + "\n")  # Sauvegarde des notes dans un fichier texte
    messagebox.showinfo("Sauvegarde", "Les notes ont été sauvegardées dans 'notes.txt'.")

def charger_notes():
    try:
        with open("notes.txt", "r") as file:
            for line in file:
                notes.append(line.strip())  # On ajoute chaque ligne du fichier à la liste des notes
                listbox_notes.insert(tk.END, line.strip())  # On affiche chaque note dans la liste
        messagebox.showinfo("Chargement", "Les notes ont été chargées depuis 'notes.txt'.")
    except FileNotFoundError:
        messagebox.showwarning("Fichier non trouvé", "Aucun fichier de notes trouvé.")

# Création de la fenêtre principale
window = tk.Tk()
window.title("Carnet de Notes")

# Zone d'entrée pour la note
entry_note = tk.Entry(window, width=40)
entry_note.pack(pady=10)

# Liste des notes affichées (avec défilement possible)
listbox_notes = tk.Listbox(window, width=40, height=10)
listbox_notes.pack(pady=10)

# Boutons pour ajouter, supprimer, sauvegarder et charger des notes
button_ajouter = tk.Button(window, text="Ajouter Note", command=ajouter_note)
button_ajouter.pack(pady=5)

button_supprimer = tk.Button(window, text="Supprimer Note", command=supprimer_note)
button_supprimer.pack(pady=5)

button_sauvegarder = tk.Button(window, text="Sauvegarder Notes", command=sauvegarder_notes)
button_sauvegarder.pack(pady=5)

button_charger = tk.Button(window, text="Charger Notes", command=charger_notes)
button_charger.pack(pady=5)

# Charger les notes au démarrage de l'application
charger_notes()

# Lancer la boucle principale de l'interface graphique
window.mainloop()
