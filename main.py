import sys
from exercice import Exercice

#typst compile output_file.typ

def lire_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r') as fichier:
            contenu = fichier.read()
            print(f"Contenu du fichier {nom_fichier} :\n{contenu}")
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'existe pas.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 composition.py fichier1 fichier2 ...")
        sys.exit(1)
    args=["typ/doc1.typ", "typ/doc2.typ"]
    
    listexo = [] 
    for nom_fichier in args:
        # lire_fichier(nom_fichier)
        exercises = Exercice.load_exercises_from_file(nom_fichier)  
        listexo.extend(exercises)  

    # Display the loaded exercises
    for exercise in enumerate(listexo, start=1):
        Exercice.display_exercice(exercise)
        print("ha")
    
    
if __name__ == "__main__":
    main()
