import sys
from exercise import Exercice

def lire_fichier(filename):
    try:
        with open(filename, 'r') as fichier:
            content = fichier.read()
            print(f"File contents {filename} :\n{content}")
    except FileNotFoundError:
        print(f"File {filename} does not exist.")

def main():
    if len(sys.argv) < 2:
        print("Use: python3 main.py file1 file2 ...")
        sys.exit(1)
    
    output = open("output_file.typ", "w")

        
    args= sys.argv
    
    
    #fusion de fichier 
    for file in args[1:]:
        print(file)
        f = open(file, "r")
        output.write("\n= New file : " + file + "\n")
        content = f.read()
        output.write(content)
        
    print("to have the output in pdf: typst compile output_file.typ")
    
    
    
if __name__ == "__main__":
    main()
