notes = []

def ajouter_note(note):
    notes.append(note)
    print("Note ajoutée!")

def afficher_notes():
    if not notes:
        print("Aucune note disponible.")
    else:
        print("\nListe des notes:")
        for i, note in enumerate(notes, start=1):
            print(f"{i}. {note}")

def supprimer_note(index):
    try:
        removed_note = notes.pop(index - 1)
        print(f"Note '{removed_note}' supprimée.")
    except IndexError:
        print("Note non trouvée.")

def sauvegarder_notes():
    with open("notes.txt", "w") as file:
        for note in notes:
            file.write(note + "\n")
    print("Notes sauvegardées dans 'notes.txt'.")

def charger_notes():
    try:
        with open("notes.txt", "r") as file:
            for line in file:
                notes.append(line.strip())
        print("Notes chargées depuis 'notes.txt'.")
    except FileNotFoundError:
        print("Aucun fichier de notes trouvé.")

def menu():
    print("\nCarnet de notes")
    print("1. Ajouter une note")
    print("2. Afficher les notes")
    print("3. Supprimer une note")
    print("4. Sauvegarder les notes")
    print("5. Charger les notes")
    print("6. Quitter")

    choix = input("Choisissez une option: ")
    return choix

# Charger les notes au démarrage
charger_notes()

while True:
    choix = menu()

    if choix == "1":
        note = input("Entrez la note: ")
        ajouter_note(note)
    elif choix == "2":
        afficher_notes()
    elif choix == "3":
        afficher_notes()
        index = int(input("Entrez le numéro de la note à supprimer: "))
        supprimer_note(index)
    elif choix == "4":
        sauvegarder_notes()
    elif choix == "5":
        charger_notes()
    elif choix == "6":
        print("Merci d'avoir utilisé le carnet de notes!")
        break
    else:
        print("Choix invalide!")
